# Microservice-based Application Assignment

It is time to put everything you have learnt so far into practice. The goal of this assignment is for you to create a microservice-based application according to the following principles:

- The application must be deployable using Kubernetes.
- The application must consist of at least two different types of microservices.
- Each microservice must implement a REST API for access.
- The application must be accessible from “the outside” (e.g. via a web browser).
- All microservices in the application must be horizontally scalable independently from each other.
- Any microservice images required to run your application must have been pushed to Docker Hub so that Kubernetes may find them.
- The application must make use of some form of database running as a separate microservice.
- The database must use storage that is persistent across restarts of the deployment infrastructure.
- The database does not have to be scalable.

## Deliverables

The following items shall be delivered:

1. A description of the software you have built and what it does.
2. A software architecture design of your application, describing the role of each component in your system, their responsibilities, and the architecture principles (e.g. cloud architecture patterns) that are used to connect them to a functioning system. This also includes a mapping between software components and the microservices designed and built to implement the components.
3. A discussion of the benefits and challenges with your architecture design. This must include a discussion about security. It must also include a discussion of what you have done or what can be done to mitigate the identified challenges.
4. A link to a configuration management repository (e.g. git) where the source code of the application can be viewed. This must also include the code for your Kubernetes deployment.

## Presentation Meeting

Once delivered, a meeting will be scheduled where you are expected to run and explain your application and its deployment. Be prepared to answer questions about:

- Your software application idea
- The architecture design decisions in your application
- The business implications of these architecture decisions
- Interaction between different microservices
- Details of your deployment
- Security issues identified and/or mitigated

## Additional Information

Your application:

- May implement any software idea; it may also be a copy of an already existing software.
- May be too small or trivial to actually warrant scaling; please acknowledge this and provide instructions for what needs to be pretended for the application to make sense.
- May use any programming language.
- May use a different access interface than a web browser, as long as no additional tools need to be installed on my computer.
- May use any type of database (e.g. NoSQL, SQL, Graph, etc.).
- May be deployed to a cloud provider already.

There is a Quiz on Canvas where you can submit your article summaries and answers to the questions.

**NOTICE:** This is a marked assignment that contributes to the grade on the course. Specifically, the assignment contributes to your grade on the following parts of the course:

- Cloud Provisioning and Deployment
- The Business Case for Cloud Computing
