from .profile import PROFILE

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
