# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Audit(models.Model):
    logs = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)

class PrismaMigrations(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_prisma_migrations'


class AgentInvitations(models.Model):
    connectioninvitation = models.TextField(db_column='connectionInvitation')  # Field name made lowercase.
    multiuse = models.BooleanField(db_column='multiUse')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.IntegerField(db_column='lastChangedBy')  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    agentid = models.ForeignKey('OrgAgents', models.DO_NOTHING, db_column='agentId')  # Field name made lowercase.
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId')  # Field name made lowercase.
    recipientkey = models.TextField(db_column='recipientKey', blank=True, null=True)  # Field name made lowercase.
    invitationdid = models.TextField(db_column='invitationDid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agent_invitations'


class Agents(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    name = models.TextField()
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'agents'


class AgentsType(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    agent = models.CharField(max_length=500)
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'agents_type'


class Cities(models.Model):
    name = models.TextField()
    state = models.ForeignKey('States', models.DO_NOTHING)
    state_code = models.TextField()
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    country_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'cities'


class CloudWalletUserInfo(models.Model):
    id = models.UUIDField(primary_key=True)
    label = models.TextField(blank=True, null=True)
    tenantid = models.TextField(db_column='tenantId', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=500, blank=True, null=True)
    type = models.TextField()  # This field type is a guess.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId', blank=True, null=True)  # Field name made lowercase.
    agentapikey = models.TextField(db_column='agentApiKey', blank=True, null=True)  # Field name made lowercase.
    agentendpoint = models.TextField(db_column='agentEndpoint', blank=True, null=True)  # Field name made lowercase.
    key = models.TextField(blank=True, null=True)
    connectionimageurl = models.TextField(db_column='connectionImageUrl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cloud_wallet_user_info'


class Connections(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    connectionid = models.TextField(db_column='connectionId', unique=True)  # Field name made lowercase.
    state = models.TextField()
    id = models.UUIDField(primary_key=True)
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    theirlabel = models.TextField(db_column='theirLabel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'connections'


class Countries(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'countries'


class CredentialDefinition(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    credentialdefinitionid = models.CharField(db_column='credentialDefinitionId', max_length=500)  # Field name made lowercase.
    tag = models.CharField(max_length=500)
    schemaledgerid = models.CharField(db_column='schemaLedgerId', max_length=500)  # Field name made lowercase.
    revocable = models.BooleanField()
    id = models.UUIDField(primary_key=True)
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    schemaid = models.ForeignKey('Schema', models.DO_NOTHING, db_column='schemaId')  # Field name made lowercase.
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'credential_definition'


class Credentials(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    connectionid = models.TextField(db_column='connectionId', blank=True, null=True)  # Field name made lowercase.
    threadid = models.TextField(db_column='threadId', unique=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    credentialexchangeid = models.TextField(db_column='credentialExchangeId')  # Field name made lowercase.
    state = models.TextField()
    schemaid = models.TextField(db_column='schemaId')  # Field name made lowercase.
    creddefid = models.TextField(db_column='credDefId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'credentials'


class Ecosystem(models.Model):
    name = models.TextField()
    description = models.TextField()
    tags = models.TextField(blank=True, null=True)
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    logourl = models.TextField(db_column='logoUrl', blank=True, null=True)  # Field name made lowercase.
    autoendorsement = models.BooleanField(db_column='autoEndorsement')  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    ledgers = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecosystem'


class EcosystemConfig(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.TextField(db_column='lastChangedBy')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecosystem_config'


class EcosystemInvitations(models.Model):
    email = models.TextField()
    status = models.TextField()
    userid = models.TextField(db_column='userId')  # Field name made lowercase.
    orgid = models.TextField(db_column='orgId')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    ecosystemid = models.ForeignKey(Ecosystem, models.DO_NOTHING, db_column='ecosystemId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecosystem_invitations'


class EcosystemOrgs(models.Model):
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId')  # Field name made lowercase.
    status = models.TextField()
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    deploymentmode = models.TextField(db_column='deploymentMode', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    ecosystemid = models.ForeignKey(Ecosystem, models.DO_NOTHING, db_column='ecosystemId')  # Field name made lowercase.
    ecosystemroleid = models.ForeignKey('EcosystemRoles', models.DO_NOTHING, db_column='ecosystemRoleId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecosystem_orgs'


class EcosystemRoles(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecosystem_roles'


class EcosystemUsers(models.Model):
    userid = models.TextField(db_column='userId')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    ecosystemid = models.ForeignKey(Ecosystem, models.DO_NOTHING, db_column='ecosystemId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecosystem_users'


class EndorsementTransaction(models.Model):
    endorserdid = models.TextField(db_column='endorserDid')  # Field name made lowercase.
    authordid = models.TextField(db_column='authorDid')  # Field name made lowercase.
    requestpayload = models.TextField(db_column='requestPayload')  # Field name made lowercase.
    responsepayload = models.TextField(db_column='responsePayload')  # Field name made lowercase.
    status = models.TextField()
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    type = models.TextField(blank=True, null=True)
    requestbody = models.JSONField(db_column='requestBody', blank=True, null=True)  # Field name made lowercase.
    resourceid = models.TextField(db_column='resourceId', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    ecosystemorgid = models.ForeignKey(EcosystemOrgs, models.DO_NOTHING, db_column='ecosystemOrgId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'endorsement_transaction'


class FileData(models.Model):
    referenceid = models.TextField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.
    error = models.TextField(blank=True, null=True)
    detailerror = models.TextField(db_column='detailError', blank=True, null=True)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    iserror = models.BooleanField(db_column='isError', blank=True, null=True)  # Field name made lowercase.
    creddefid = models.TextField(db_column='credDefId', blank=True, null=True)  # Field name made lowercase.
    schemaid = models.TextField(db_column='schemaId', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField()
    credential_data = models.JSONField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    fileuploadid = models.ForeignKey('FileUpload', models.DO_NOTHING, db_column='fileUploadId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    credential_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_data'


class FileUpload(models.Model):
    name = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    upload_type = models.TextField(blank=True, null=True)
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    credential_type = models.TextField(blank=True, null=True)
    templateid = models.CharField(db_column='templateId', blank=True, null=True, max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'file_upload'


class Ledgerconfig(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    details = models.JSONField()
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.TextField(db_column='lastChangedBy')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ledgerConfig'


class Ledgers(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    name = models.CharField(max_length=500)
    networktype = models.CharField(db_column='networkType', max_length=500)  # Field name made lowercase.
    poolconfig = models.CharField(db_column='poolConfig', max_length=500)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive')  # Field name made lowercase.
    networkstring = models.CharField(db_column='networkString', max_length=500)  # Field name made lowercase.
    nymtxnendpoint = models.CharField(db_column='nymTxnEndpoint', max_length=500)  # Field name made lowercase.
    indynamespace = models.CharField(db_column='indyNamespace', blank=True, null=True, max_length=500)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    networkurl = models.CharField(db_column='networkUrl', blank=True, null=True, max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ledgers'


class Notification(models.Model):
    id = models.UUIDField(primary_key=True)
    orgid = models.UUIDField(db_column='orgId', unique=True, blank=True, null=True)  # Field name made lowercase.
    notificationwebhook = models.TextField(db_column='notificationWebhook', blank=True, null=True)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.TextField(db_column='lastChangedBy')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notification'


class OrgAgents(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    orgdid = models.CharField(db_column='orgDid', blank=True, null=True, max_length=500)  # Field name made lowercase.
    verkey = models.CharField(blank=True, null=True, max_length=500)
    agentendpoint = models.CharField(db_column='agentEndPoint', blank=True, null=True, max_length=500)  # Field name made lowercase.
    isdidpublic = models.BooleanField(db_column='isDidPublic', blank=True, null=True)  # Field name made lowercase.
    agentspinupstatus = models.IntegerField(db_column='agentSpinUpStatus', blank=True, null=True)  # Field name made lowercase.
    agentoptions = models.BinaryField(db_column='agentOptions', blank=True, null=True)  # Field name made lowercase.
    walletname = models.CharField(db_column='walletName', blank=True, null=True, max_length=500)  # Field name made lowercase.
    tenantid = models.TextField(db_column='tenantId', blank=True, null=True)  # Field name made lowercase.
    apikey = models.TextField(db_column='apiKey', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    agentid = models.ForeignKey(Agents, models.DO_NOTHING, db_column='agentId', blank=True, null=True)  # Field name made lowercase.
    agentstypeid = models.ForeignKey(AgentsType, models.DO_NOTHING, db_column='agentsTypeId', blank=True, null=True)  # Field name made lowercase.
    orgid = models.OneToOneField('Organisation', models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    orgagenttypeid = models.ForeignKey('OrgAgentsType', models.DO_NOTHING, db_column='orgAgentTypeId', blank=True, null=True)  # Field name made lowercase.
    ledgerid = models.ForeignKey(Ledgers, models.DO_NOTHING, db_column='ledgerId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    webhookurl = models.CharField(db_column='webhookUrl', blank=True, null=True, max_length=500)  # Field name made lowercase.
    diddocument = models.JSONField(db_column='didDocument', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'org_agents'


class OrgAgentsType(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    agent = models.CharField(max_length=500)
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'org_agents_type'


class OrgDids(models.Model):
    id = models.UUIDField(primary_key=True)
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    orgid = models.UUIDField(db_column='orgId')  # Field name made lowercase.
    did = models.CharField(max_length=500)
    diddocument = models.JSONField(db_column='didDocument')  # Field name made lowercase.
    orgagentid = models.ForeignKey(OrgAgents, models.DO_NOTHING, db_column='orgAgentId')  # Field name made lowercase.
    isprimarydid = models.BooleanField(db_column='isPrimaryDid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'org_dids'


class OrgInvitations(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField()
    orgroles = models.TextField(db_column='orgRoles', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    orgid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='orgId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'org_invitations'


class OrgRoles(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.TextField(db_column='lastChangedBy')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'org_roles'


class Organisation(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    name = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    orgslug = models.TextField(db_column='orgSlug', unique=True, blank=True, null=True)  # Field name made lowercase.
    logourl = models.TextField(db_column='logoUrl', blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(blank=True, null=True, max_length=500)
    publicprofile = models.BooleanField(db_column='publicProfile')  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    clientid = models.CharField(db_column='clientId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clientsecret = models.CharField(db_column='clientSecret', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idpid = models.CharField(db_column='idpId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    registrationnumber = models.CharField(db_column='registrationNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='cityId', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Countries, models.DO_NOTHING, db_column='countryId', blank=True, null=True)  # Field name made lowercase.
    stateid = models.ForeignKey('States', models.DO_NOTHING, db_column='stateId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organisation'


class PlatformConfig(models.Model):
    externalip = models.CharField(db_column='externalIp', max_length=500)  # Field name made lowercase.
    username = models.CharField(max_length=500)
    sgapikey = models.CharField(db_column='sgApiKey', max_length=500)  # Field name made lowercase.
    emailfrom = models.CharField(db_column='emailFrom', max_length=500)  # Field name made lowercase.
    apiendpoint = models.CharField(db_column='apiEndpoint', max_length=500)  # Field name made lowercase.
    tailsfileserver = models.CharField(db_column='tailsFileServer', max_length=500)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    lastchangedby = models.TextField(db_column='lastChangedBy')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    inboundendpoint = models.CharField(db_column='inboundEndpoint', blank=True, null=True, max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platform_config'


class Presentations(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    connectionid = models.TextField(db_column='connectionId', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    threadid = models.TextField(db_column='threadId', unique=True)  # Field name made lowercase.
    isverified = models.BooleanField(db_column='isVerified', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    orgid = models.ForeignKey(Organisation, models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    presentationid = models.TextField(db_column='presentationId', blank=True, null=True)  # Field name made lowercase.
    schemaid = models.CharField(db_column='schemaId', blank=True, null=True, max_length=500)  # Field name made lowercase.
    emailid = models.TextField(db_column='emailId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'presentations'


class Schema(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    name = models.CharField( max_length=500)
    version = models.CharField( max_length=500)
    attributes = models.TextField()
    schemaledgerid = models.CharField(db_column='schemaLedgerId', max_length=500)  # Field name made lowercase.
    publisherdid = models.CharField(db_column='publisherDid', max_length=500)  # Field name made lowercase.
    issuerid = models.CharField(db_column='issuerId', max_length=500)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    orgid = models.ForeignKey(Organisation, models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.
    ledgerid = models.ForeignKey(Ledgers, models.DO_NOTHING, db_column='ledgerId', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'schema'


class ShorteningUrl(models.Model):
    referenceid = models.CharField(db_column='referenceId', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(blank=True, null=True, max_length=500)
    id = models.UUIDField(primary_key=True)
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    invitationpayload = models.JSONField(db_column='invitationPayload', blank=True, null=True)  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shortening_url'


class States(models.Model):
    name = models.TextField()
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    country_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'states'


class Token(models.Model):
    id = models.UUIDField(primary_key=True)
    token = models.TextField(unique=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    expiresat = models.DateTimeField(db_column='expiresAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'token'


class User(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=500, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    verificationcode = models.CharField(db_column='verificationCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isemailverified = models.BooleanField(db_column='isEmailVerified')  # Field name made lowercase.
    supabaseuserid = models.CharField(db_column='supabaseUserId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clientsecret = models.CharField(db_column='clientSecret', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profileimg = models.TextField(db_column='profileImg', blank=True, null=True)  # Field name made lowercase.
    fidouserid = models.CharField(db_column='fidoUserId', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    isfidoverified = models.BooleanField(db_column='isFidoVerified')  # Field name made lowercase.
    publicprofile = models.BooleanField(db_column='publicProfile')  # Field name made lowercase.
    password = models.CharField(blank=True, null=True, max_length=500)
    id = models.UUIDField(primary_key=True)
    keycloakuserid = models.CharField(db_column='keycloakUserId', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UserActivity(models.Model):
    action = models.TextField()
    details = models.TextField()
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    orgid = models.ForeignKey(Organisation, models.DO_NOTHING, db_column='orgId')  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_activity'


class UserCredentials(models.Model):
    imageurl = models.TextField(db_column='imageUrl', blank=True, null=True)  # Field name made lowercase.
    credentialid = models.TextField(db_column='credentialId', unique=True)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_credentials'


class UserDevices(models.Model):
    createdatetime = models.DateTimeField(db_column='createDateTime')  # Field name made lowercase.
    lastchangeddatetime = models.DateTimeField(db_column='lastChangedDateTime')  # Field name made lowercase.
    devices = models.JSONField(blank=True, null=True)
    credentialid = models.CharField(db_column='credentialId', unique=True, blank=True, null=True, max_length=500)  # Field name made lowercase.
    devicefriendlyname = models.CharField(db_column='deviceFriendlyName', blank=True, null=True, max_length=500)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
    authcounter = models.IntegerField(db_column='authCounter')  # Field name made lowercase.
    id = models.UUIDField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.UUIDField(db_column='createdBy')  # Field name made lowercase.
    lastchangedby = models.UUIDField(db_column='lastChangedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_devices'


class UserOrgDeleteActivity(models.Model):
    id = models.UUIDField(primary_key=True)
    userid = models.UUIDField(db_column='userId')  # Field name made lowercase.
    orgid = models.UUIDField(db_column='orgId')  # Field name made lowercase.
    recordtype = models.TextField(db_column='recordType')  # Field name made lowercase. This field type is a guess.
    txnmetadata = models.JSONField(db_column='txnMetadata')  # Field name made lowercase.
    deletedby = models.UUIDField(db_column='deletedBy')  # Field name made lowercase.
    deletedatetime = models.DateTimeField(db_column='deleteDateTime')  # Field name made lowercase.
    useremail = models.TextField(db_column='userEmail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_org_delete_activity'


class UserOrgRoles(models.Model):
    id = models.UUIDField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    orgroleid = models.ForeignKey(OrgRoles, models.DO_NOTHING, db_column='orgRoleId')  # Field name made lowercase.
    orgid = models.ForeignKey(Organisation, models.DO_NOTHING, db_column='orgId', blank=True, null=True)  # Field name made lowercase.
    idproleid = models.UUIDField(db_column='idpRoleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_org_roles'


class UserRole(models.Model):
    id = models.UUIDField(primary_key=True)
    role = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user_role'


class UserRoleMapping(models.Model):
    id = models.UUIDField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    userroleid = models.ForeignKey(UserRole, models.DO_NOTHING, db_column='userRoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_role_mapping'
