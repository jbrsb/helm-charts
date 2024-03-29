# Bootstrap of Datasetup Init File

import logging


from datahub.emitter.mce_builder import make_domain_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.metadata.schema_classes import ChangeTypeClass, DomainPropertiesClass

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

domain_urn = make_domain_urn("marketing")
domain_properties_aspect = DomainPropertiesClass(
    name="Marketing", description="Entities related to the marketing department"
)

event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
    entityType="domain",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=domain_urn,
    aspect=domain_properties_aspect,
)

rest_emitter = DatahubRestEmitter(gms_server="https://tenant.env.account.semarchy.net/api/intelligence/catalog")
rest_emitter.emit(event)
log.info(f"Created domain {domain_urn}")
