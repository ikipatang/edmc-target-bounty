- Useful [python online editor](https://www.tutorialspoint.com/execute_python_online.php)
- Python lint [pep8online](http://pep8online.com/)

## Scan stage

```json
{ "timestamp":"2018-08-14T21:15:30Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"anaconda", "ScanStage":0 }
{ "timestamp":"2018-08-14T21:15:31Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"anaconda", "ScanStage":1, "PilotName":"$npc_name_decorate:#name=Andy Beard;", "PilotName_Localised":"Andy Beard", "PilotRank":"Elite" }
{ "timestamp":"2018-08-14T21:15:33Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"anaconda", "ScanStage":2, "PilotName":"$npc_name_decorate:#name=Andy Beard;", "PilotName_Localised":"Andy Beard", "PilotRank":"Elite", "ShieldHealth":100.000000, "HullHealth":100.000000 }
{ "timestamp":"2018-08-14T21:15:35Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"anaconda", "ScanStage":3, "PilotName":"$npc_name_decorate:#name=Andy Beard;", "PilotName_Localised":"Andy Beard", "PilotRank":"Elite", "ShieldHealth":100.000000, "HullHealth":100.000000, "Faction":"LHS 20 Organisation", "LegalStatus":"Wanted", "Bounty":293350 }
{ "timestamp":"2018-08-14T22:34:19Z", "event":"ShipTargeted", "TargetLocked":false }
```

### Wanted status
```json
{
  "timestamp": "2018-08-14T17:54:01Z",
  "event": "ShipTargeted",
  "TargetLocked": true,
  "Ship": "diamondback",
  "Ship_Localised": "Diamondback Scout",
  "ScanStage": 3,
  "PilotName": "$npc_name_decorate:#name=Kugai Atomsk;",
  "PilotName_Localised": "Kugai Atomsk",
  "PilotRank": "Expert",
  "ShieldHealth": 100.000000,
  "HullHealth": 100.000000,
  "Faction": "LHS 1604 Silver Partnership",
  "LegalStatus": "Wanted",
  "Bounty": 127575
}
```

### Legal status

```json
{
  "timestamp": "2018-08-14T17:53:53Z",
  "event": "ShipTargeted",
  "TargetLocked": true,
  "Ship": "diamondback",
  "Ship_Localised": "Diamondback Scout",
  "ScanStage": 3,
  "PilotName": "$npc_name_decorate:#name=Sirius Security;",
  "PilotName_Localised": "Sirius Security",
  "PilotRank": "Competent",
  "ShieldHealth": 100.000000,
  "HullHealth": 100.000000,
  "Faction": "Li Yong-Rui",
  "LegalStatus": "Clean"
}
```