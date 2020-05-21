*This is the test project for practising some technologies.*

**"Tideas"** is the application for teachers to share their ideas about learning materials that they need in the teaching process.
Here author can share an idea and other teachers can vote for it. Application assumes that there is another group of user - methodologists - who will take the most popular ideas to work and share the prepared learning material to help teachers in their work.
Also, application should contain a blog for knowledge/materials sharing and discussions.


**Main tools**: Flask, PostgreSQL, SQLAlchemy, alembic, Docker, marshmallow(flask-restful adaptation).

**In future**: pytest, React, Jenkins, EKL, Redis, MongoDB, AWS services(S3?), Swagger and others

This is one of the services for "tideas" application designed using micro-services architecture with RESTfull approach:
* project_api service
* UI service service
* user_api service
* document_api service
* blog_api service
* and others

**To run app:**

```
git clone https://github.com/ddanilenko/projects
cd projects
docker-compose up -d --build
```