#!/bin/bash
fission spec init
fission env create --spec --name suitability-env --image nexus.sigame.com.br/fission-async:0.1.6 --builder nexus.sigame.com.br/python-builder-3.8:0.0.2
fission fn create --spec --name suitability-fn --env suitability-env --src "./func/*" --entrypoint main.create_suitability_profile  --executortype newdeploy --rpp 100000
fission route create --spec --method POST --url /suitability --function suitability-fn
