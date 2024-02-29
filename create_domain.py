import logging

from datahub.emitter.mce_builder import make_domain_urn
from datahub.emitter.mcp import MetadataChangeProposalWrapper
from datahub.emitter.rest_emitter import DatahubRestEmitter
from datahub.metadata.schema_classes import ChangeTypeClass, DomainPropertiesClass
from datahub.ingestion.run.pipeline import Pipeline
import sys

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

args = sys.argv[1:]

if len(args) != 2:
    print("Usage: python3 create_domain.py <xdg_gms_url> <xdg_token>")
    sys.exit(1)

xdg_gms_url = sys.argv[1]
xdg_token = sys.argv[2]

domain_urn = make_domain_urn("sales")
domain_properties_aspect = DomainPropertiesClass(
    name="Sales", description="""### Overview
    
In the dynamic landscape of business, effective data governance is paramount, and nowhere is this more evident than in the realm of Sales. In the Sales domain, where success hinges on insightful decision-making and customer-centric strategies, robust data governance emerges as the linchpin for sustained growth and competitive advantage.

### Sales Governance

***Sales data governance*** involves the meticulous management, quality assurance, and strategic utilization of data throughout its lifecycle. From prospecting to closing deals and beyond, a comprehensive data governance framework ensures that information is accurate, timely, and aligned with organizational goals. It empowers sales teams with the confidence that the data driving their efforts is reliable, fostering a culture of data-driven decision-making.

### Activities

This domain's data governance encompasses a spectrum of **activities**, including data **standardization**, **privacy compliance**, and seamless **integration** across diverse systems. By fostering a centralized and standardized approach to data management, sales organizations can streamline operations, reduce redundancy, and uncover actionable insights. Furthermore, stringent data governance in Sales is a testament to an organization's commitment to data ethics and regulatory compliance, instilling trust among customers and partners.

In essence, Sales data governance is the cornerstone for elevating sales performance, enhancing customer relationships, and navigating the evolving landscape of modern business with precision and confidence.

**This domain and its contents are provided for Demo Purposes**
"""
)

event: MetadataChangeProposalWrapper = MetadataChangeProposalWrapper(
    entityType="domain",
    changeType=ChangeTypeClass.UPSERT,
    entityUrn=domain_urn,
    aspect=domain_properties_aspect,
)

rest_emitter = DatahubRestEmitter(xdg_gms_url, xdg_token)
rest_emitter.emit(event)
log.info(f"Created domain {domain_urn}")

# Harversters

# The pipeline configuration is similar to the recipe YAML files provided to the CLI tool.

# pipeline = Pipeline.create(
#     {
#         "source": {
#             "type": "mysql",
#             "config": {
#                 "username": "user",
#                 "password": "pass",
#                 "database": "db_name",
#                 "host_port": "localhost:3306",
#             },
#         },
#         "sink": {
#             "type": "datahub-rest",
#             "config": {"server": "http://localhost:8080"},
#         },
#     }
# )
#
# # Run the pipeline and report the results.
# pipeline.run()
# pipeline.pretty_print_summary()