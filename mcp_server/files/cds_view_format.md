# ABAP CDS Basic Interface View Format

Use this as the formatting reference when creating a CDS view for a different
table. Keep the annotation sections in this order and include the client
element in the projection. Replace every placeholder with a value appropriate
to the requested table; do not copy VBBE names, fields, labels, or descriptions.

```abap
// ----- Layer 1: @AbapCatalog -----
@AbapCatalog.sqlViewName: '<unique_sql_view_name>'
@AbapCatalog.viewEnhancementCategory: [#NONE]

// ----- Layer 2: @ClientHandling -----
@ClientHandling.type: #CLIENT_DEPENDENT

// ----- Layer 3: @AccessControl -----
@AccessControl.authorizationCheck: #NOT_REQUIRED

// ----- Layer 4: @EndUserText -----
@EndUserText.label: '<business label>'

// ----- Layer 5: @Metadata -----
@Metadata.ignorePropagatedAnnotations: true
@Metadata.allowExtensions: true

// ----- Layer 6: @VDM -----
@VDM.viewType: #BASIC

// ----- Layer 7: @ObjectModel -----
@ObjectModel: {
  representativeKey: ['<representative_key>'],
  usageType: {
    serviceQuality: #C,
    sizeCategory: #L,
    dataClass: #MASTER
  },
  supportedCapabilities: [ #CDS_MODELING_DATA_SOURCE, #ANALYTICAL_DIMENSION ]
}

// ----- Layer 8: @Analytics -----
@Analytics: {
  dataExtraction: {
    enabled: true,
    delta.changeDataCapture.automatic: true
  }
}

define view <view_name> as select from <source_table>
{
  key <source_key> as <KEY_ALIAS>,
      <source_field> as <FIELD_ALIAS>,
      $session.client as clnt
}
```

Use the requested table's verified key fields for `representativeKey` and the
projection. Adjust table-specific annotation values when the available
metadata requires it. Do not invent fields or keys: if the workspace has no
reliable schema information for the requested table, ask for its field/key
definitions or clearly state what could not be verified.
