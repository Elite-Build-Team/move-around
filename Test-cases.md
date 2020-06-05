% Test cases v1.0
% Move around
% ![](images/Logo.jpg)

\newpage

## Μέλη ομάδας
* Δήμτσας Γιάννης 1054423
* Μαντάς Ελευθέριος 1047128
* Ρούστας Κωνσταντίνος 1054422
* Συμεωνίδης Θεόδωρος 1064870

## Editor
* Δήμτσας Γιάννης 1054423
* Μαντάς Ελευθέριος 1047128
* Ρούστας Κωνσταντίνος 1054422
* Συμεωνίδης Θεόδωρος 1064870

## Peer Reviewer
* Δήμτσας Γιάννης 1054423
* Μαντάς Ελευθέριος 1047128
* Ρούστας Κωνσταντίνος 1054422
* Συμεωνίδης Θεόδωρος 1064870

## Εργαλεία
Markdown, VSCode, GanttProject, Pandoc, Lightshot, [Table generator](https://www.tablesgenerator.com/), [Mockflow](https://www.mockflow.com/), VisualParadigm, [Diagrams.net](https://app.diagrams.net/)

![Test Cases](/images/Test-Cases-v0.1.png)

|  Test Case ID |  Test Scenario| Test Steps| Test Data | Expected Results  |  Actual Results | Pass/Fail  ||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|01 |  Valid Issue Description Type | 1. Click "Report Issue" </br> 2. Choose Location & Submit </br> 3. Choose Photograph & Submit  </br> 4. Insert Description   | description = "This is a test that is supposed to pass" |  After storing description, user returns to App Main Screen. | As Expected  | Pass |
|02 |  Invalid Issue Description Type | 1. Click "Report Issue" </br> 2. Choose Location & Submit </br> 3. Choose Photograph & Submit  </br> 4. Insert Description   | description = "12345" |  Show pop-up TypeError message | As Expected  | Pass |
|03 |  Valid Photograph Type |  1. Click "Report Issue" </br> 2. Choose Location & Submit </br> 3. Choose Photograph & Submit | photograph = "images/Risk-Assessment-Form-Testing.png"  |  Store photograph and show Issue Description Screen. | As Expected  | Pass  |
|04   | Invalid Photograph Type  | 1. Click "Report Issue" </br> 2. Choose Location & Submit </br> 3. Choose Photograph & Submit  |  photograph ="tables/testing.tgn"  |  Show TypeError message | As Expected  | Pass  |
|05  |  Valid Location | 1. Click "Report Issue" </br> 2. Choose Location & Submit  | location = (38.245982, 21.739000)   | Pass the Location to report issue location and show choose photograph screen  | As Expected  | Pass  |
|06   |  Invalid Location |  1. Click "Report Issue" </br> 2. Choose Location & Submit   |  location = (-37.616667, 57.933333) |  Error : Location out of PATRAS |  Not Expected | Fail  |