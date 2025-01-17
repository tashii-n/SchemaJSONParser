from django.shortcuts import render
import requests
import json
from .models import Organisation, OrgDids, Schema, Ledgers, Audit
from datetime import datetime, timezone, timedelta
import uuid

def format_schema(schema_data):
    """
    Transform schema data into the required format with timestamps in the specified format.
    """
    if not isinstance(schema_data, dict):
        raise ValueError("Expected schema_data to be a dictionary")

    formatted_attributes = []

    for key, value in schema_data.items():
        # Skip keys where the value is not a dictionary
        if not isinstance(value, dict):
            continue

        if key == "id":
            continue

        formatted_attributes.append({
            "isRequired": True,
            "attributeName": key,
            "schemaDataType": value.get("type", "string"),
            "displayName": value.get("title", key),
        })

    return json.dumps(formatted_attributes)


def extract_version(url):
    # Split the URL by slashes and retrieve the middle part
    parts = url.strip('/').split('/')

    # print("URL:", url)
    # Check if there is a middle part and return it
    if len(parts) > 2:
        middle_value = parts[3]  # This would get the version, e.g., 'draft-07'
        return middle_value
    else:
        return 'Invalid URL format'


def extract_and_format_time(input_str):
    # Split the input string at the last hyphen
    datetime_str = input_str.rsplit('-', 1)[0]

    # Convert the string to a datetime object (handling 'Z' for UTC)
    dt_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Apply the timezone offset (for example, +6 hours)
    tz = timezone(timedelta(hours=6))

    # Format the datetime object and return it in the desired format
    formatted_time = dt_obj.replace(tzinfo=timezone.utc).astimezone(
        tz).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + "+06"

    return formatted_time


def home(request):
    current_time = datetime.now(timezone(timedelta(hours=6))).strftime(
        "%Y-%m-%d %H:%M:%S.%f")[:-3] + "+06"
    createDateTime = None
    lastChangedDateTime = current_time
    attributes = None
    error_message = None
    schema_name = None
    version = None
    schemaLedgerId = None
    publisherDid = None
    issuerId = None
    id = None
    orgId = None
    createdBy = None
    lastChangedBy = None
    ledgerId = None
    type = None
    organisations = Organisation.objects.using('secondary').exclude(
        id__in=OrgDids.objects.filter(did__icontains='indy').values('orgid'))

    if request.method == "POST":
        submit_type = request.POST.get("submit_type")

        if submit_type == "single":
            # Process single schema URL submission
            schema_url = request.POST.get("schema_url")
            ledgerId = request.POST.get('ledgerID')
            orgId = request.POST.get("organisation_id")
            org = Organisation.objects.using('secondary').get(id=orgId)
            orgDid = OrgDids.objects.using('secondary').get(orgid=orgId)
            ledgerIDMain = Ledgers.objects.using('secondary').get(id=ledgerId)

            try:
                # Make the request to fetch schema data
                response = requests.get(schema_url)
                response.raise_for_status()
                schema_data = response.json()

                # Extract necessary data
                createDateTime = extract_and_format_time(schema_data['$id'])
                schema_name = schema_data['title']
                version = extract_version(schema_data['$schema'])
                schemaLedgerId = schema_url
                publisherDid = orgDid.did
                issuerId = orgDid.did
                id = str(uuid.uuid4())
                createdBy = org.createdby
                lastChangedBy = org.lastchangedby
                ledgerId = ledgerId
                type = 'w3c'

                # Extract credentialSubject properties
                credential_subject_properties = schema_data['definitions']['credentialSubject']['properties']
                attributes = format_schema(credential_subject_properties)

                # Save the schema to the database
                Schema.objects.using('secondary').create(
                    createdatetime=createDateTime,
                    lastchangeddatetime=lastChangedDateTime,
                    name=schema_name,
                    version=version,
                    attributes=attributes,
                    schemaledgerid=schemaLedgerId,
                    publisherdid=publisherDid,
                    issuerid=issuerId,
                    id=id,
                    orgid=org,
                    createdby=createdBy,
                    lastchangedby=lastChangedBy,
                    ledgerid=ledgerIDMain,
                    type=type
                )

                # Create an audit log for the schema creation, including all the data
                audit_log = f"""
                Created schema with the following details:
                Schema URL: {schema_url}
                Schema Name: {schema_name}
                Version: {version}
                Created DateTime: {createDateTime}
                Last Changed DateTime: {lastChangedDateTime}
                Org ID: {orgId}
                Org Name: {org.name}
                Publisher DID: {publisherDid}
                Issuer DID: {issuerId}
                Ledger ID: {ledgerId}
                Attributes: {attributes}
                Created By: {createdBy}
                Last Changed By: {lastChangedBy}
                Schema Ledger ID: {schemaLedgerId}
                Type: {type}
                """

                Audit.objects.create(
                    logs=audit_log.strip(),
                    timestamp=datetime.now(timezone(timedelta(hours=6)))
                )

            except requests.exceptions.RequestException as e:
                error_message = f"Failed to fetch schema: {e}"
                # Log the error in the audit
                Audit.objects.create(
                    logs=f"Error occurred while fetching schema URL {
                        schema_url}: {e}",
                    timestamp=datetime.now(timezone(timedelta(hours=6)))
                )
            except json.JSONDecodeError:
                error_message = "The response is not valid JSON."
                # Log the JSON error in the audit
                Audit.objects.create(
                    logs=f"Invalid JSON response from schema URL {schema_url}",
                    timestamp=datetime.now(timezone(timedelta(hours=6)))
                )

    # Render the updated template with all the data
    return render(request, 'parser/index.html', {
        "attributes": attributes,
        "schema_name": schema_name,
        "version": version,
        "schemaLedgerId": schemaLedgerId,
        "publisherDid": publisherDid,
        "issuerId": issuerId,
        "id": id,
        "orgId": orgId,
        "createdBy": createdBy,
        "lastChangedBy": lastChangedBy,
        "ledgerId": ledgerId,
        "type": type,
        "error_message": error_message,
        "organisations": organisations,
        "createDateTime": createDateTime,
        "lastChangedDateTime": lastChangedDateTime,
    })
