# Azure Red Hat OpenShift azure-cli extension

## Install extension

Using `azdev` tool add extension repo:
```
azdev extension repo add /home/mjudeiki/go/src/github.com/mjudeikis/azure-cli-aro
zdev extension add aro-preview
```

## Dev RP

To run CLI commands for dev CLI you will need to set env `BASE_URL`
to `BASE_URL=https://localhost:8443/`.

Disable ssl check for CLI:
`export AZURE_CLI_DISABLE_CONNECTION_VERIFICATION=1`

Manually register subscription to fakeRP. In production this will be done via
`ARM` endpoint.

```
curl -k -X PUT "https://localhost:8443/subscriptions/$AZURE_SUBSCRIPTION_ID?api-version=2.0" -H 'Content-Type: application/json' -d '{"state": "Registered", "properties": {"tenantId": "'"$AZURE_TENANT_ID"'"}}'
```

## Examples

Create a cluster when CLI created RH and VNET:
```
az aro-preview create --resource-group clustername-v4 -n clustername-test --location=eastus --client-id=$AZURE_CLIENT_ID --client-secret=$AZURE_CLIENT_SECRET --provider-client-id=$AZURE_FP_CLIENT_ID
```

Create a clueter with BYO vnet rg:
az aro-preview create --resource-group clustername--vnet-rg-name clustername-vnet -n clustername-test --loc
ation=eastus --client-id=$AZURE_CLUSTER_CLIENT_ID --client-secret=$AZURE_CLUSTER_CLIENT_SECRET

## Vendoring new SDK

When vendoring dev version of aro cli, extend `AzureRedHatOpenShiftClientConfiguration`:
```
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if os.environ.get('BASE_URL') != "":
             base_url = os.environ.get('BASE_URL')
        if not base_url:
            base_url = 'https://management.azure.com'
```
