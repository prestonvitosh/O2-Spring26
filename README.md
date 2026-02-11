# InspirEd: A medical education app

## Group A CS 4273 Spring 2026

### Description

InspirEd is a medical education application, specifically designed for education surrounding rare lung diseases. It is made to adapt to the user's level of knowledge to provide the most pertinent and useful information regarding these specific diseases. An LLM is used to connect the user to prewritten education modules pertaining to the given disease, ensuring that correct and usable information is given to the user.

### Other apps and sources

There aren't any existing apps and sites that provide infromation about rare lung diseases that is correct, thorough, meaningful, easy, and catered to the level of knowledge that the user possesses.

- Since these diseases are rare, most families who encounter them don't know much about them beforehand.
  - For the same reason, there isn't much readily available information nor apps with such information.
  - Additionally, the information found online and even the information provided to the families from their physicians is either not thorough or correct enough, or it involves excessively complex and difficult terms that the patients and their families cannot understand the diseases well enough.
  - This lack of knowledge can result in a lack of proper action and overall uncertainty or discomfort.
- When doctors tell their patients and their families about the lung diseases, much of the information is hard to understand and even to hear, such as with large and rare words like hydroxychloroquine and surfactant.
  - There aren't any apps that properly adapt to the user's level of knowledge in the subject. This is one of the biggest issues with educating about these rare diseases.
  - When a user is provided with information above their level, they are bombarded with a flood of difficult information and are left not knowing what to do.
  - When a user is given information below their level, they are left not knowing quite what they need to know and may be frustrated.
- Current AI usage in this field is insufficient, whether in a standalone app, in a medical website's AI chat box, or on an AI app or site like ChatGPT.
  - Since this has to deal with rare lung diseases, large language models aren't quite there, at least not yet, and usually base facts, claims, and even diagnoses on information that is actually solely related to other diseases, sypmtoms, etc.
  - Essentially, as it stands, when LLMs try to provide information about these rare diseases, they fabricate much of the information they convey to the users.
 
### Requirements and key features

Because of these problems, key requirements and features can be identified:
- Adaptive scaffolding to tier learning and provide information to the user based on their level of knowledge
- Database with disease information provided by experts and moderators, not by LLMs
- An LLM to link the user to these modules based on their needs and level of knowledge, solely to provide confirmed information, not diagnoses
- An easy way for educators and the client to successfully add modules
- A well-documented path for the client to edit the interface, add modules, run the database, and any other pertinent moderation actions
- Inclusion of the prior scribe feature to transcribe a doctor's visit in real time for keywords

### Development platforms

- The designs will be made in Figma, where we will primarily focus on the mobile app interface
- Most of the current app has been developed in React Native in Expo Go, and we will continue this
- We will make a new database in Google Firebase
- We will use Google Gemini for the AI LLM

### Goals and progress
- By 02/15, have a working database with mock health education information in tiered modules
- By 03/08, have a working LLM to link to modules
- By 03/29, successfully implement adaptive scaffolding
- By 04/12, alter and fine-tune the design of the interface to our liking and our client's
- By 05/03, thoroughly document necessary moderation actions for the client and, if applicable, the next steps for the client or a future development team

### Team members and roles

- Preston
  - Product Owner
- Drydin
  - Sprint Master 1
- Camellia
  - Sprint Master 2
- Sudhiksha
  - Sprint Master 3
- Henry
  - Sprint Master 4
