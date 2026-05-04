from fasthtml.common import *

from ui.components import page_shell
from content import PROFILE


def products_page():
    return page_shell(
        f"Services | {PROFILE['name']}",
        "/products",
        Section(
            H2("Consulting & Services", cls="title"),
            P(
                "Specialized data engineering and platform architecture solutions.",
                cls="subtitle muted",
            ),
            cls="section",
        ),
        Section(
            Div(
                Article(
                    H3("Services"),
                    H4("Data Platform Architecture"),
                    P(
                        "End-to-end design of modern data stacks, focusing on Snowflake, BigQuery, and K8s."
                    ),
                    cls="card",
                ),
                Article(
                    H3("Services"),
                    H4("Pipeline Optimization"),
                    P(
                        "Performance tuning for Spark and Airflow to reduce cloud costs and improve stability."
                    ),
                    cls="card",
                ),
                Article(
                    H3("Services"),
                    H4("Data Quality & Governance"),
                    P(
                        "Implementing automated testing, lineage tracking, and schema contract monitoring."
                    ),
                    cls="card",
                ),
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;",
            ),
            cls="section",
        ),
    )
