# Day 17 - Code shipping & Deployment 🚢

## Overview

Welcome to day 17! This day will be all about learning how code is being shipped from development to production, and how it is deployed using Openshift. You will be focusing on a tool that enables `revision management` on Openshift objects - `helm`, and an automation platform - `Argo` that integrates with helm (and other tools) to automatically deploy k8s (short for kubernetes) or OS (short for Openshift) objects.

Today, you will not be given exact reading material, like a book/links. Part of the exercise is looking up sources in the internet. Instead, you will be given guiding questions that will assist you in looking up subjects or topics.

## Goals

- Learn how helm integrated with k8s and OS.
- Learn how Argo is used as a general automation platform.
- Learn how Argo is used with helm to automate `helm chart` deployment.
- Hone the skill of learning subjects by yourself with little to no assistance.

## Time limit

The time limit for this session is a day and a half.

## Helm guiding questions

1. What is helm and what problem does it solve in k8s?
2. What is a helm chart? what are the main components that comprise a helm chart?
3. How do you "run" a helm chart over an Openshift namespace?
4. What is a `values.yaml` file?
5. How do initialize a helm chart from scratch? What is its basic directory structure?
6. How do you define dependencies between charts?\
7. What is the difference between `helm uninstall` and `helm delete`?
8. How to rollback a helm installation to a previous revision?
9. How do you debug a `helm install/upgrade` statement if it fails? Which tools/commands would you use?

## Argo guiding questions

1. What is Argo? How is it used to create automations?
1. Explain the difference between Argo and Argo CD.
1. What are the main components of an Argo workflow? Explain
1. Research how to define an Argo workflow. Which basic parameters are mandatory to define a basic Argo workflow?
1. How to create an automation that automatically deploys a chart that changes were pushed into?
1. What are `step` and `template` in Argo?
1. Read about error handling in Argo workflows.

## Discussion

Approach your mentor to discuss the subjects you have learned and verify your knowledge.
The discussion will be about all the material you have studied in the days of `Docker` `Openshift` and today.

## Wrapping up

Congrats, you have successfully finished chapter 3! You are now qualified to start contributing code to the group's codebases, be proud! 🎉🎉🎉

Congratulations for completing day 17!

Approach your mentor, if you have time remaining in your development onboarding, you may move onto the `appendix.md` in chapter 3.
