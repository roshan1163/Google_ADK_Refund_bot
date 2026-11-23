# ABAP CDS View for SAP AUSP Table (Characteristic Values)

This document provides SAP Core Data Services (CDS) view definitions for reading object classification and characteristic values from the SAP **AUSP** table, including associations to characteristic master data (**CABN** and **CABNT**).

---

## 📌 Overview

- **Database Table**: `AUSP` (Characteristic Values)
- **Primary Use Case**: Retrieve classification characteristic values assigned to objects (e.g., Materials, Equipment, Batches, Notifications).
- **Joined/Associated Tables**:
  - `CABN` - Characteristic Master (maps `ATINN` to `ATNAM`)
  - `CABNT` - Characteristic Language-Dependent Descriptions

---

## 1. Basic CDS View: `ZI_CharacteristicValues`

This basic CDS view exposes the raw `AUSP` fields with data conversions and annotations.

```abap
@AbapCatalog.sqlViewName: 'ZICHARVAL'
@AbapCatalog.compiler.compareFilter: true
@AbapCatalog.preserveKey: true
@AccessControl.authorizationCheck: #CHECK
@EndUserText.label: 'CDS View for Characteristic Values (AUSP)'

define view ZI_CharacteristicValues
  as select from ausp as Ausp

  association [0..1] to cabn  as _Characteristic     on  $projection.InternalCharNum = _Characteristic.atinn
  association [0..*] to cabnt as _CharacteristicText on  $projection.InternalCharNum = _CharacteristicText.atinn
                                                     and _CharacteristicText.spras   = $session.system_language
{
  key Ausp.objek as ObjectKey,
  key Ausp.atinn as InternalCharNum,
  key Ausp.atzis as CharacteristicValueCounter,
  key Ausp.mafid as ObjectIndicator,
  key Ausp.klart as ClassType,
  key Ausp.adzum as ChangeNumber,

      -- Characteristic Name from CABN
      _Characteristic.atnam                  as CharacteristicName,

      -- Characteristic Values
      Ausp.atwrt                             as CharValueText,
      Ausp.atflv                             as CharValueFromNum,
      Ausp.atawe                             as UnitOfMeasureFrom,
      Ausp.atsfl                             as CharValueToNum,
      Ausp.ataw1                             as UnitOfMeasureTo,
      Ausp.atcod                             as CodeForValueRange,
      Ausp.attab                             as ReferenceTableName,
      Ausp.atfel                             as ReferenceFieldName,
      Ausp.atvar                             as VariantKey,

      -- Associations
      _Characteristic,
      _CharacteristicText
}
```

---

## 2. Enhanced CDS View with Characteristic Name & Description

This view joins `CABN` and `CABNT` directly to provide human-readable characteristic names (`ATNAM`) and descriptions (`ATBEZ`).

```abap
@AbapCatalog.sqlViewName: 'ZICHARVALEXT'
@AbapCatalog.compiler.compareFilter: true
@AbapCatalog.preserveKey: true
@AccessControl.authorizationCheck: #CHECK
@EndUserText.label: 'CDS View for Object Classification & Values'

define view ZI_ObjectCharacteristicValue
  as select from ausp as Ausp
    inner join   cabn as Cabn  on Ausp.atinn = Cabn.atinn
    left outer join cabnt as Cabnt on  Cabn.atinn  = Cabnt.atinn
                                   and Cabnt.spras = $session.system_language
{
  key Ausp.objek                     as ObjectKey,
  key Cabn.atnam                     as CharacteristicName,
  key Ausp.klart                     as ClassType,
  key Ausp.atzis                     as ValueCounter,
      Ausp.atinn                     as InternalCharNum,
      Cabnt.atbez                    as CharacteristicDescription,
      Ausp.mafid                     as ObjectIndicator,
      Ausp.atwrt                     as CharValueText,
      Ausp.atflv                     as CharValueFromNum,
      Ausp.atsfl                     as CharValueToNum,
      Ausp.atawe                     as UnitOfMeasure,
      Ausp.adzum                     as ChangeNumber
}
```

---

## 3. Key Fields Explanation

| Field Name (AUSP) | Data Element | Description |
| :--- | :--- | :--- |
| `OBJEK` | `CUOBN` | Key of object to be classified (e.g., Material Number `MATNR`, Equipment `EQUNR`) |
| `ATINN` | `ATINN` | Internal Characteristic Number (links to `CABN-ATINN`) |
| `ATZIS` | `ATZIS` | Characteristic Value Counter (for multi-value characteristics) |
| `MAFID` | `KLMAF` | Indicator: Object (`O`) or Class (`K`) |
| `KLART` | `KLASSENART` | Class Type (e.g., `001` Material Class, `023` Batch Class) |
| `ATWRT` | `ATWRT` | Characteristic Value (Char/Text format) |
| `ATFLV` | `ATFLV` | Internal Floating-Point Value From (Numeric characteristic value) |
| `ATSFL` | `ATSFL` | Internal Floating-Point Value To (Numeric range upper limit) |

---

## 💡 Usage Notes & SAP Best Practices

1. **Performance Tip**: `AUSP` is a large table in SAP systems. Always filter on `KLART` (Class Type) and `OBJEK` or `ATINN` in your query WHERE clauses or consumption views.
2. **Numeric Values (`ATFLV`)**: `ATFLV` stores numeric values as IEEE floating-point numbers. If you need integer/decimal conversions, use SAP built-in functions like `FLTP_TO_DEC` or cast in CDS / ABAP code.
3. **Multi-Value Characteristics**: An object can have multiple values for a single characteristic. `ATZIS` differentiates multiple values for the same `OBJEK` and `ATINN`.
