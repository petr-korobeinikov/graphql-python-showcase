# graphql-python-showcase

### Stop using REST, Post-JSON, and other stuff from 2k00.

## Running

```shell
DOCKER_BUILDKIT=1 docker build -t graphql-python-showcase .
docker run --rm -p 9000:9000 graphql-python-showcase
```

Open `http://<your-docker-host>:9000/`.

![graphiql](graphiql.png)

## An example set of queries

### Find all projects

```graphql
query allProjects {
    projects {
        id
        name
        slug
    }
}
```

### Find all project names

```graphql
query allProjectNames {
    projects {
        name
    }
}
```

### Find all project with tasks

```graphql
query allProjectsWithTasks {
    projects {
        id
        name
        tasks {
            id
            title
        }
    }
}
```

### Find project by slug (query variable demo)

```graphql
query projectBySlug($slug: String!) {
    projectBySlug(slug: $slug) {
        id
        name
        slug
    }
}
```

Provide a required `slug` variable:

```json
{
    "slug": "proj1"
}
```

### Using directive example

```graphql
query projectWithTasksBySlug($slug: String!, $withTasks: Boolean!) {
    projectBySlug(slug: $slug) {
        id
        name
        slug
        tasks @include(if: $withTasks) {
            id
            title
        }
    }
}
```

```json
{
    "slug": "proj1",
    "withTasks": true
}
```

### Find assignees

```graphql
query projectBySlug ($slug: String!) {
    projectBySlug(slug: $slug) {
        id
        name
        slug
        tasks {
            id
            title
            assignee {
                id
                name
            }
        }
    }
}

```

## TODO

Add:

* Mutations
* Pagination
* Fragments
* Auth

## Python + GraphQL quick start

* [docs.graphene-python.org/en/latest/quickstart/](https://docs.graphene-python.org/en/latest/quickstart/)
* [www.starlette.io/graphql/](https://www.starlette.io/graphql/)

## Main GraphQL learning resource

* [graphql.org](https://graphql.org/)
* [graphql.org/learn/](https://graphql.org/learn/)

## Free learning resources

* [www.howtographql.com](https://www.howtographql.com)
* [www.graphqlweekly.com](https://www.graphqlweekly.com/)

## Paid learning resources

* [app.pluralsight.com/library/courses/graphql-big-picture/table-of-contents](https://app.pluralsight.com/library/courses/graphql-big-picture/table-of-contents)
* [egghead.io/courses/graphql-query-language](https://egghead.io/courses/graphql-query-language)
* [egghead.io/courses/designing-graphql-schemas-99db](https://egghead.io/courses/designing-graphql-schemas-99db)
* [packtpub.com/application-development/beginning-graphql-elearning](https://www.packtpub.com/application-development/beginning-graphql-elearning)
* [packtpub.com/application-development/practical-graphql-become-graphql-ninja-video](https://www.packtpub.com/application-development/practical-graphql-become-graphql-ninja-video)
* [packtpub.com/web-development/hands-full-stack-web-development-graphql-and-react](https://www.packtpub.com/web-development/hands-full-stack-web-development-graphql-and-react)
