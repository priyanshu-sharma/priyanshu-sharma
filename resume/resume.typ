#set page(
  paper: "us-letter",
  margin: (x: 0.75in, y: 0.6in),
)

#set text(
  font: "SF Pro Text",
  size: 10pt,
  fill: rgb("#1a1a1a"),
  tracking: 0.1pt,
)

#set par(
  leading: 0.75em,
  spacing: 0.75em,
  justify: true,
)

#set list(
  indent: 12pt,
  body-indent: 6pt,
  spacing: 0.8em,
)

#show heading: set text(font: "SF Pro Text", fill: rgb("#003366"), weight: "semibold")

#let section_title(title) = {
  v(18pt, weak: true)
  heading(level: 1, title)
  v(-2pt)
  line(length: 100%, stroke: 0.5pt + gray)
  v(4pt)
}

#let job(company: "", role: "", date: "", location: "", body_content) = {
  block(width: 100%, breakable: true)[
    #grid(
      columns: (1fr, auto),
      row-gutter: 6pt,
      [#text(font: "FiraCode Nerd Font", weight: "semibold", size: 10.5pt)[#role]],
      [#set align(right); #text(font: "FiraCode Nerd Font", size: 10.5pt, weight: "semibold")[#date]],

      [#text(font: "FiraCode Nerd Font", weight: "medium", size: 9pt, fill: rgb("#444444"))[#company]],
      [#set align(right); #text(
        font: "FiraCode Nerd Font",
        size: 9pt,
        fill: rgb("#444444"),
        weight: "medium",
      )[#location]],
    )
    #v(4pt)
    #body_content
  ]
  v(14pt)
}

#align(center)[
  #text(weight: "medium", size: 26pt)[PRIYANSHU SHARMA] \
  #v(6pt)
  #text(font: "FiraCode Nerd Font", size: 10pt, weight: "semibold")[
    prynsh1112\@gmail.com #h(-4pt) | #h(-4pt)
    +1(858)-305-8168 #h(-4pt) | #h(-4pt)
    Manhattan, NY #h(-4pt) | #h(-4pt)
    priyanshu-sharma.dev.com
  ]
]

#section_title("Professional Summary")

#par(justify: true)[
  *Senior Data Engineer II* specializing in designing and scaling *petabyte-scale distributed data platforms* across *on-prem systems and cloud environments (AWS, GCP, Azure, Oracle)*. Experienced in building *high-throughput real-time and batch streaming pipelines, large-scale data migrations, and performance-optimized data architectures*. Focused on enabling *low-latency analytics, resilient data systems, and enterprise-scale data processing*.
]

#section_title("Education")

#grid(
  columns: (1fr, auto),
  row-gutter: 10pt,

  [#text(font: "FiraCode Nerd Font", weight: "semibold")[M.S. in Computer Science]],
  [#set align(right); #text(font: "FiraCode Nerd Font", weight: "semibold")[September 2022 - June 2024]],

  [#text(font: "FiraCode Nerd Font", weight: "regular")[University of California, Riverside]],
  [#set align(right); #text(font: "FiraCode Nerd Font", weight: "regular")[Los Angeles, CA]],

  [#text(font: "FiraCode Nerd Font", weight: "semibold")[B.Tech. in Computer Science]],
  [#set align(right); #text(font: "FiraCode Nerd Font", weight: "semibold")[July 2015 - March 2019]],

  [#text(font: "FiraCode Nerd Font", weight: "regular")[Vellore Institute of Technology]],
  [#set align(right); #text(font: "FiraCode Nerd Font", weight: "regular")[Chennai, IN]],
)

#section_title("Technology Skills")

  #grid(
    columns: (2in, 1fr),
    row-gutter: 12pt,

    text(font: "FiraCode Nerd Font", weight: "regular")[*Languages*],
    [Python, SQL(PostgreSQL, BigQuery, Snowflake Dialects), Bash, Scala, R.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Cloud Platform*],
    [On-Premises, Amazon Web Services (AWS), Google Cloud Platform (GCP), Azure, Oracle, Cloudera/Hortonworks Hadoop Environments.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Data Engineering*],
    [Apache Spark (Structured Streaming, API, SQL), Apache Kafka, Apache Flink, Delta Lake, Apache Iceberg, dbt, Pandas, Ray, Pyspark, Sqoop.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Orchestration*],
    [Apache Airflow, Dagster, Prefect, AWS Step Functions, Azure Data Factory, Logic Apps.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Storage & Warehouse*],
    [Apache Druid, Snowflake, BigQuery, Redshift, Teradata, Amazon S3, Azure Data Lake Storage (ADLS), GCS, Delta Lake, Hive.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Databases*],
    [PostgreSQL, MySQL, Oracle, AmazonRDS, Redis, MongoDB, Cassandra, HBase, DynamoDB, Bigtable.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Infrastructure*],
    [Kubernetes (GKS/EKS), Docker, Terraform, Helm.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Security & Ops*],
    [IAM, VPC, DLP, Jenkins, GitHub, GitLab, CI/CD Pipelines, Ansible.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Visualization*],
    [Tableau, Power BI, QuickSight, Looker, Kibana, Data Studio, Grafana.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Project Methods*],
    [Agile, Scrum, Test-Driven Development (TDD), Unit Testing, Functional Testing, Design Thinking.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*AWS Data Services*],
    [Amazon EMR, AWS Glue, Amazon Kinesis, Amazon MSK (Kafka), AWS Lake Formation, Amazon Redshift Spectrum, Amazon EC2, EMR, Lambda, Glue, Athena, MSK, SNS, SQS, CloudWatch, CDK.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*GCP Data Services*],
    [BigQuery, Dataflow, Dataproc, Pub/Sub, Cloud Storage, Vertex AI Pipelines.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*Azure Data Services*],
    [Azure Data Factory, Azure Databricks, Azure Synapse Analytics, Azure Stream Analytics, Azure Data Lake Storage.],

    text(font: "FiraCode Nerd Font", weight: "regular")[*OCI Data Services*],
    [OCI Data Flow, OCI Object Storage, OCI Streaming, OCI Data Integration, Autonomous Data Warehouse, OCI Data Catalog.], 
)

#section_title("Professional Experience")

#job(
  company: "Verizon Wireless Inc.",
  role: "Senior Data Engineer - II",
  date: "November 2024 – Present",
  location: "Basking Ridge, NJ",
)[
  - Owned and operated petabyte-scale, real-time data processing systems on-prem using Spark Structured Streaming with Kafka, enabling low-latency, high-throughput pipelines; implemented data transformations with dbt and built analytical data stores using Apache Druid for real-time querying.
  - Built and optimized batch and streaming data pipelines using PySpark, Scala, Spark SQL/DataFrames, and Hive (HiveQL, partitions), incorporating CDC (Change Data Capture) to process high-volume structured and semi-structured data from MySQL, NoSQL, Snowflake, MongoDB, and REST APIs.
  - Architected real-time data streaming systems using Kafka (MSK), Kinesis, and Spark Streaming, enabling reliable, low-latency data flow across Databricks, Redshift, Lambda, and downstream systems.
  - Designed and orchestrated workflows using Apache Airflow (DAGs) and AWS Lambda; automated CI/CD pipelines with Jenkins and Terraform for infrastructure provisioning and deployment across Glue, EMR, Kinesis, and Redshift.
  - Implemented robust observability and security practices using CloudWatch, CloudTrail, and Microsoft Intune, enforcing encryption, DLP, and access controls; ensured data integrity through rigorous ETL validation and testing.
  - Developed GenAI-enabled data engineering workflows, preparing and curating large-scale datasets for LLM-based applications, and building pipelines to support model training, inference, and data retrieval use cases.
  - Developed GenAI-powered data engineering systems by building end-to-end RAG (Retrieval-Augmented Generation) pipelines using vector databases (Pinecone / FAISS), embedding workflows with OpenAI and Hugging Face models, and orchestrating LLM workflows for enterprise search and data intelligence use cases.
  - Engineered data pipelines to support LLM applications, including document ingestion, chunking, embedding generation, and retrieval pipelines using LangChain and LlamaIndex integrated with structured and streaming data sources.
  - Led cross-functional teams and owned full data lifecycle (design → deployment), driving performance, scalability, and cost optimization across distributed systems and Big Data platforms.
  - Built and optimized scalable, high-performance APIs to support real-time data access and ingestion across distributed data platforms, ensuring low-latency interaction between streaming and batch systems.
]

#job(
  company: "Johnson & Johnson R&D",
  role: "Senior Data Engineer I",
  date: "January 2024 – October 2024",
  location: "Raritan, NJ",
)[
  - Architected and implemented scalable data platforms on GCP, leveraging Cloud Storage Transfer Service, Cloud Storage (GCS), BigQuery, Bigtable, and Pub/Sub for secure ingestion, storage, and event-driven processing of structured and unstructured data.
  - Built and optimized batch and real-time data pipelines using Apache Spark (Scala, PySpark), Dataflow, and Dataproc (YARN), integrating with Hive, Pig, Kafka, Hadoop, HBase, and Cassandra for large-scale distributed processing.
  - Designed and orchestrated ETL/ELT workflows using Cloud Composer (Apache Airflow), including custom operators/sensors, CDC-based ingestion from Oracle, and automated pipeline scheduling and monitoring via Cloud Monitoring.
  - Developed and governed data models across BigQuery and Snowflake, implementing DBT for transformation, schema evolution, data versioning, and data quality validation; enabled downstream analytics via Tableau, Looker, and Data Studio.
  - Defined cross-platform data architecture integrating GCP, Snowflake, and Oracle; implemented infrastructure provisioning with Terraform, container orchestration with Kubernetes, and IAM-based access control for secure, cost-optimized environments.
  - Led advanced analytics and ML workflows using Vertex AI Pipelines, Apache Spark, and scikit-learn; improved system performance and cost efficiency through Cloud Billing insights, resource optimization, and mentoring junior engineers on ETL and Snowflake best practices.
]

#job(
  company: "Wells Fargo & Company",
  role: "Senior Data Intern",
  date: "April 2023 - December 2023",
  location: "New York City, NY",
)[
  - Migrated and orchestrated ETL workflows using Azure Data Factory, moving data from Oracle and SQL Server to Azure Blob Storage, Data Lake Storage, and Azure SQL Data Warehouse based on workload requirements.
  - Built and optimized large-scale data processing pipelines using Azure Databricks (Scala, PySpark), leveraging RDD caching, DataFrames, and Spark transformations to process terabyte-scale datasets from Blob Storage and diverse sources (JSON, databases, structured files).
  - Designed and optimized Hive-based data models on Azure HDInsight, implementing partitioning strategies for efficient data segmentation and improved query performance.
  - Enabled real-time data processing using Azure Stream Analytics and orchestrated workflows with Logic Apps; ensured system observability and performance tracking via Azure Monitor.
  - Implemented secure data access and migration practices using Azure Active Directory and Key Vault, ensuring encryption, access control, and data integrity across RDBMS (MySQL, SQL Server) and NoSQL systems.
  - Developed automated data workflows and supporting infrastructure using Python, Scala, and UNIX shell scripting across Azure Linux VMs; delivered analytics solutions via Tableau and Power BI for business insights.
]

#job(
  company: "KayaPay (Stealth Startup)",
  role: "Founding Data Intern",
  date: "December 2022 – March 2023",
  location: "San Francisco, CA",
)[
  - Designed and architected the end-to-end backend for the KayaConnect platform, enabling seamless communication between contractors (home constructors) and clients.
  - Developed and deployed RESTful APIs for client onboarding, project management, and communication workflows; integrated backend services with a React + TypeScript frontend.
  - Built cloud-native data ingestion and transformation workflows using patterns aligned with Oracle Cloud Infrastructure services such as Object Storage, Data Integration, and Data Flow (Apache Spark) for scalable data processing.
  - Designed streaming and event-driven data pipelines inspired by OCI Streaming and Service Connector Hub, enabling real-time data movement and system decoupling.
  - Modeled and managed structured data workflows aligned with Autonomous Data Warehouse and Oracle Database systems, supporting analytics and transactional use cases.
  - Implemented metadata management and data discovery practices aligned with OCI Data Catalog to improve data visibility and governance.
  - Applied observability patterns to OCI Logging and Monitoring to track system performance and debug data pipelines.
]

#job(
  company: "Blinkit",
  role: "Senior Software Engineer",
  date: "January 2021 - September 2022",
  location: "Bangalore, IN",
)[
  - Architected and scaled cloud-native data platforms on AWS using S3, Athena, Glue (Python), Redshift, and Databricks (PySpark), enabling efficient data collection, transformation, and analytics workflows.
  - Built and orchestrated batch and streaming pipelines using AWS Step Functions, Kinesis, Apache Spark Streaming, and Amazon MSK (Kafka); executed large-scale Spark/Hadoop jobs on EMR with data sourced from S3 and DynamoDB.
  - Developed and optimized ETL frameworks using AWS Glue, PySpark, and Python; translated SQL logic into Spark transformations and implemented in-memory data processing for high-performance workloads.
  - Designed secure, scalable infrastructure using EC2 (load-balanced), Lambda (Python), and RDS/MySQL/NoSQL systems; implemented encryption, access controls, and fine-tuned database/query performance for high-throughput systems.
  - Led data migration initiatives from legacy systems to MySQL and NoSQL databases, ensuring data integrity, security, and minimal downtime.
  - Established observability and deployment pipelines using CloudWatch, CloudTrail, Jenkins, CodePipeline, and CodeDeploy; containerized Kafka (Confluent) workloads with secure subnet configurations and managed version control via Git.
]

#job(
  company: "Blinkit",
  role: "Software Engineer",
  date: "January 2019 - December 2020",
  location: "Bangalore, IN",
)[
  - Designed and built scalable data pipelines across the Hadoop ecosystem using Pig, Hive (HQL, external tables), HBase, and MapReduce; performed large-scale data profiling and transformation with Python and Oracle.
  - Engineered high-throughput ingestion systems using Sqoop (RDBMS → HDFS, CSV) and Flume (real-time log streaming), processing millions of structured records.
  - Optimized distributed data processing using Apache Spark (Spark Context, Spark SQL, DataFrames, Paired RDDs, YARN) with Scala, improving performance of legacy Hadoop workloads.
  - Developed and orchestrated ETL pipelines using Apache NiFi, enabling automated, fault-tolerant data movement and transformation.
  - Built and scaled distributed backend systems (30+ services) using Django, Spring Boot, and Go; implemented asynchronous processing with Python Celery, improving memory utilization by 8–12%, and applied CQRS with PostGIS integration for real-time, geospatial data processing.
  - Led migration of 10+ microservices (Elixir, Java, Python, .NET) to Managed RabbitMQ and Elasticache, reducing API latency by 27%; improved database performance via B+ and R+ index optimization and standardized Micro-Frontend architecture using Runtime Module Federation to accelerate iteration by 5–10%.
]