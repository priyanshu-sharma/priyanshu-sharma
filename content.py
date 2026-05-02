PROFILE = {
    "name": "Priyanshu Sharma",
    "role": "Senior Data Engineer | Machine Learning Specialist | Full Stack Developer",
    "email": "priyanshu@example.com",
    "resume_path": "/resume",
    "availability": "Open to Senior Data Engineer roles and consulting engagements.",
}

SITE = {
    "name": PROFILE["name"],
    "title": f"{PROFILE['name']} | {PROFILE['role']}",
    "description": (
        "Priyanshu Sharma is a Senior Data Engineer building reliable data "
        "systems with Python, Spark, Airflow, Kafka, dbt, and cloud infrastructure."
    ),
    "author": PROFILE["name"],
    "keywords": "Priyanshu Sharma, Senior Data Engineer, Python, Spark, Airflow, Kafka, dbt",
    "url": "http://127.0.0.1:4000",
    "api_title": f"{PROFILE['name']} API",
    "api_description": "API routes for the Priyanshu Sharma portfolio site.",
    "api_version": "1.0.0",
}

HOME = {
    "title": "Building reliable data systems at scale",
    "subtitle": "I design and maintain modern data platforms using Python, SQL, Spark, orchestration, and cloud infrastructure.",
    "badges": ["Python", "Spark", "Airflow", "Kafka", "dbt"],
    "philosophy": "I believe that data systems should be boring, scalable, and self-documenting. Reliability isn't a feature; it's the foundation of every architectural decision.",
    "learning": "Currently deepening my understanding of Rust and its potential for high-performance data processing pipelines.",
    "setup": "MacBook Pro M3, VS Code, iTerm2, and Obsidian for knowledge management.",
}

PROJECTS = {
    "title": "Projects",
    "subtitle": "Selected data engineering work delivered in production environments.",
    "items": [
        {
            "tag": "Realtime Platform",
            "title": "Streaming Ingestion Pipeline",
            "desc": "Event-driven processing with quality checks and low-latency serving for analytics consumers.",
            "demo_href": "https://example.com/streaming-ingestion-demo",
        },
        {
            "tag": "Analytics",
            "title": "Lakehouse KPI Layer",
            "desc": "Built trusted transformation models and orchestration for reliable cross-functional reporting.",
            "demo_href": "https://example.com/lakehouse-kpi-demo",
        },
        {
            "tag": "Machine Learning",
            "title": "Feature Pipeline Framework",
            "desc": "Implemented batch/stream feature generation with lineage and reproducible backfills.",
            "demo_href": "https://example.com/feature-pipeline-demo",
        },
        {
            "tag": "Data Quality",
            "title": "Contract Monitoring Service",
            "desc": "Automated schema drift alerts and rule-based validation for upstream data contracts.",
            "demo_href": "https://example.com/contract-monitoring-demo",
        },
        {
            "tag": "Infrastructure",
            "title": "IaC Cluster Provisioner",
            "desc": "Terraform modules for standardized K8s cluster lifecycle management across environments.",
            "demo_href": "https://example.com/iac-demo",
        },
        {
            "tag": "Ops",
            "title": "Cost Anomaly Dashboard",
            "desc": "Real-time spend monitoring with automated Slack alerts for cloud resource over-allocation.",
            "demo_href": "https://example.com/cost-demo",
        },
    ],
}

EXPERIENCE = {
    "title": "Experience",
    "subtitle": "Platform engineering, analytics infrastructure, and reliability operations.",
    "roles": [
        {
            "title": "Senior Data Engineer",
            "summary": "Led data platform modernization, ownership of orchestration and observability.",
            "details": "Stack: Python, Spark, Airflow, dbt, Kafka, Snowflake",
        },
        {
            "title": "Data Engineer",
            "summary": "Built core ingestion and transformation pipelines for product and finance domains.",
            "details": "Focused on quality, cost optimization, and SLA reliability.",
        },
        {
            "title": "Junior Data Engineer",
            "summary": "Supported migration from legacy SQL Server to cloud-native data lake architecture.",
            "details": "Stack: SQL, Python, AWS Glue, S3",
        },
    ],
}

BLOG = {
    "title": "Blog",
    "subtitle": "Short technical notes on data engineering and platform reliability.",
    "posts": [
        {
            "date": "April 2026",
            "title": "Spark Job Tuning That Actually Reduced Costs",
            "summary": "How partition strategy, adaptive execution, and skew handling brought measurable runtime improvements.",
            "href": "#",
        },
        {
            "date": "March 2026",
            "title": "Practical Data Quality Contracts",
            "summary": "A lightweight framework for schema checks, freshness SLAs, and ownership boundaries.",
            "href": "#",
        },
        {
            "date": "February 2026",
            "title": "Airflow DAG Patterns for Stable Production Runs",
            "summary": "Patterns that improved reliability, observability, and developer velocity in orchestration workflows.",
            "href": "#",
        },
        {
            "date": "January 2026",
            "title": "Optimizing Snowflake for High Concurrency",
            "summary": "Techniques for managing virtual warehouse size and caching to serve BI tools efficiently.",
            "href": "#",
        },
    ],
}

SOCIAL = {
    "title": "Social",
    "subtitle": "Find me across professional and technical platforms.",
    "links": [
        {
            "name": "LinkedIn",
            "description": "Professional updates, role history, and data engineering highlights.",
            "href": "https://www.linkedin.com",
            "cta": "Open LinkedIn",
        },
        {
            "name": "GitHub",
            "description": "Code samples, project repositories, and experiments.",
            "href": "https://github.com",
            "cta": "Open GitHub",
        },
        {
            "name": "X / Twitter",
            "description": "Short updates, threads, and links to technical writing.",
            "href": "https://x.com",
            "cta": "Open X",
        },
        {
            "name": "Substack",
            "description": "Deep-dive technical newsletters on data systems architecture.",
            "href": "https://substack.com",
            "cta": "Read Newsletter",
        },
        {
            "name": "Email",
            "description": "Direct contact for opportunities and consulting work.",
            "href": "mailto:priyanshu@example.com",
            "cta": "Send Email",
        },
    ],
}

CONTACT = {
    "title": "Contact",
    "subtitle": PROFILE["role"],
}
