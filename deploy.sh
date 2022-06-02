#!/bin/bash
fission spec init
fission env create --spec --name suitability-env --image nexus.sigame.com.br/fission-async:0.1.6 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name suitability-fn --env suitability-env --src "./func/*" --entrypoint main.create_suitability_profile --rpp 100000
fission route create --spec --method POST --url /suitability --function suitability-fn
