# ABAP CDS View for SAP LFA1 Table (Vendor Master)

This document provides the SAP Core Data Services (CDS) basic interface view definition for reading vendor master data from the SAP **LFA1** table.

---

## 📌 Overview

- **Database Table**: `LFA1` (Vendor Master: General Data)
- **Primary Key**: `LIFNR` (Account Number of Vendor / Supplier)
- **Primary Use Case**: Basic interface view exposing core vendor master attributes.

---

## Basic Interface View: `ZI_Supplier`

```abap
// ----- Layer 1: @AbapCatalog -----
@AbapCatalog.sqlViewName: 'ZILFA1'
@AbapCatalog.viewEnhancementCategory: [#NONE]

// ----- Layer 2: @ClientHandling -----
@ClientHandling.type: #CLIENT_DEPENDENT

// ----- Layer 3: @AccessControl -----
@AccessControl.authorizationCheck: #NOT_REQUIRED

// ----- Layer 4: @EndUserText -----
@EndUserText.label: 'Vendor Master Basic View'

// ----- Layer 5: @Metadata -----
@Metadata.ignorePropagatedAnnotations: true
@Metadata.allowExtensions: true

// ----- Layer 6: @VDM -----
@VDM.viewType: #BASIC

// ----- Layer 7: @ObjectModel -----
@ObjectModel: {
  representativeKey: ['Supplier'],
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

define view ZI_Supplier as select from lfa1
{
  key lifnr as Supplier,
      name1 as SupplierName,
      name2 as SupplierName2,
      land1 as Country,
      ort01 as City,
      pstlz as PostalCode,
      regio as Region,
      stras as StreetAddress,
      adrnr as AddressID,
      anred as Title,
      sortl as SearchTerm,
      ktokk as SupplierAccountGroup,
      stcd1 as TaxNumber1,
      stcd2 as TaxNumber2,
      erdat as CreationDate,
      ernam as CreatedByUser,
      $session.client as clnt
}
```

---

## Field Mapping Reference

| Field Name (LFA1) | Key | Description |
| :--- | :--- | :--- |
| `LIFNR` | Key | Account Number of Vendor / Supplier |
| `NAME1` | | Name 1 |
| `NAME2` | | Name 2 |
| `LAND1` | | Country Key |
| `ORT01` | | City |
| `PSTLZ` | | Postal Code |
| `REGIO` | | Region (State/Province) |
| `STRAS` | | Street and House Number |
| `ADRNR` | | Address Number |
| `ANRED` | | Title |
| `SORTL` | | Search Term |
| `KTOKK` | | Vendor Account Group |
| `STCD1` | | Tax Number 1 |
| `STCD2` | | Tax Number 2 |
| `ERDAT` | | Date Record Created |
| `ERNAM` | | Name of Person who Created Object |
