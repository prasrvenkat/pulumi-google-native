// Copyright 2016-2021, Pulumi Corporation.

import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp-native";
import * as random from "@pulumi/random"

const config = new pulumi.Config("gcp-native");
const project = config.require("project");
const region = config.require("region");

const randomString = new random.RandomString("service-name", {
    upper: false,
    number: false,
    special: false,
    length: 8,
});
const serviceName = pulumi.interpolate`run-${randomString.result}`;

const service = new gcp.run.v1.Service("service", {
    projectsId: project,
    locationsId: region,
    servicesId: serviceName,
    apiVersion: "serving.knative.dev/v1",
    kind: "Service",
    metadata: {
        name: serviceName,
    },
    spec: {
        template: {
            spec: {
                containers: [{image: "gcr.io/cloudrun/hello"}],
            },
        },
    },
});

const iamHello = new gcp.run.v1.ServiceIamPolicy("allow-all", {
    projectsId: project,
    locationsId: region,
    servicesId: service.metadata.name,
    bindings: [{
        members: ["allUsers"],
        role: "roles/run.invoker",
    }],
});

export const serviceUrl = service.status.url;