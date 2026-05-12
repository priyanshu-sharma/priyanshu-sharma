from fasthtml.common import Div, H2, H3, H4, P, Section, Article

from ui_design.components import page_shell
from backend_api.content_management.models.profile import Profile


def products_page():
    # Note: Products/Services aren't explicitly in your current data models yet
    # based on the list registered in databases/init_redis.py
    # Keeping them static for now but retrieving Profile from Redis.
    profile_obj = Profile.select()[0]

    return page_shell(
        f"Services | {profile_obj.name}",
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
                Article(
                    H3("Services"),
                    H4("AI/ML Data Engineering"),
                    P(
                        "Curating large-scale datasets, RAG pipelines, and embedding workflows for LLM applications."
                    ),
                    cls="card",
                ),
                Article(
                    H3("Services"),
                    H4("Cloud Migration Strategy"),
                    P(
                        "Planning and execution of secure, cost-effective migrations from on-prem to cloud ecosystems."
                    ),
                    cls="card",
                ),
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;",
            ),
            cls="section",
        ),
    )
