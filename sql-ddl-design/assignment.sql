
-- question 1
CREATE TABLE "MedicalCenter" (
    "MedicalCenterID" int   NOT NULL,
    "Name" string   NOT NULL,
    CONSTRAINT "pk_MedicalCenter" PRIMARY KEY (
        "MedicalCenterID"
     )
);

CREATE TABLE "Doctor" (
    "DoctorID" int   NOT NULL,
    "MedicalCenterID" int   NOT NULL,
    CONSTRAINT "pk_Doctor" PRIMARY KEY (
        "DoctorID"
     )
);

CREATE TABLE "Patient" (
    "PatientID" int   NOT NULL,
    "Name" string   NOT NULL,
    CONSTRAINT "pk_Patient" PRIMARY KEY (
        "PatientID"
     )
);

CREATE TABLE "DocterPatient" (
    "DocterPatient" int   NOT NULL,
    "DoctorID" int   NOT NULL,
    "PatientID" int   NOT NULL,
    CONSTRAINT "pk_DocterPatient" PRIMARY KEY (
        "DocterPatient"
     )
);

CREATE TABLE "Visit" (
    "VisitID" int   NOT NULL,
    "PatientID" int   NOT NULL,
    "Address" string   NOT NULL,
    CONSTRAINT "pk_Visit" PRIMARY KEY (
        "VisitID"
     )
);

CREATE TABLE "Diagnosis" (
    "DiagnosisID" int   NOT NULL,
    "PatientID" int   NOT NULL,
    "DiagnosisICDCode" string   NOT NULL,
    CONSTRAINT "pk_Diagnosis" PRIMARY KEY (
        "DiagnosisID"
     )
);


--question 2
CREATE TABLE "User" (
    "UserID" int   NOT NULL,
    "PreferredRegion" string   NOT NULL,
    "Name" string   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "UserID"
     )
);

CREATE TABLE "Post" (
    "PostID" int   NOT NULL,
    "UserID" int   NOT NULL,
    "Title" string   NOT NULL,
    "Text" string   NOT NULL,
    "Location" string   NOT NULL,
    "Region" string   NOT NULL,
    "CategoryID" int   NOT NULL,
    CONSTRAINT "pk_Post" PRIMARY KEY (
        "PostID"
     )
);

CREATE TABLE "Category" (
    "CategoryID" int   NOT NULL,
    "Name" String   NOT NULL,
    CONSTRAINT "pk_Category" PRIMARY KEY (
        "CategoryID"
     )
);
CREATE TABLE "Team" (
    "TeamID" int   NOT NULL,
    "Name" string   NOT NULL,
    "Standing" int   NOT NULL,
    CONSTRAINT "pk_Team" PRIMARY KEY (
        "TeamID"
     )
);

CREATE TABLE "Goal" (
    "GoalID" int   NOT NULL,
    "PlayerID" int   NOT NULL,
    CONSTRAINT "pk_Goal" PRIMARY KEY (
        "GoalID"
     )
);

CREATE TABLE "Player" (
    "PlayerID" int   NOT NULL,
    "Name" string   NOT NULL,
    "TeamID" int   NOT NULL,
    CONSTRAINT "pk_Player" PRIMARY KEY (
        "PlayerID"
     )
);

CREATE TABLE "Match" (
    "MatchID" int   NOT NULL,
    "Team1" int   NOT NULL,
    "Team2" int   NOT NULL,
    CONSTRAINT "pk_Match" PRIMARY KEY (
        "MatchID"
     )
);

CREATE TABLE "MatchReferee" (
    "MatchRefereeID" int   NOT NULL,
    "MatchID" int   NOT NULL,
    "RefereeID" int   NOT NULL,
    CONSTRAINT "pk_MatchReferee" PRIMARY KEY (
        "MatchRefereeID"
     )
);

CREATE TABLE "Referee" (
    "RefereeID" int   NOT NULL,
    "Name" string   NOT NULL,
    CONSTRAINT "pk_Referee" PRIMARY KEY (
        "RefereeID"
     )
);

-- Free plan table limit reached. SUBSCRIBE for more.



ALTER TABLE "Doctor" ADD CONSTRAINT "fk_Doctor_MedicalCenterID" FOREIGN KEY("MedicalCenterID")
REFERENCES "MedicalCenter" ("MedicalCenterID");

ALTER TABLE "DocterPatient" ADD CONSTRAINT "fk_DocterPatient_DoctorID" FOREIGN KEY("DoctorID")
REFERENCES "Doctor" ("DoctorID");

ALTER TABLE "DocterPatient" ADD CONSTRAINT "fk_DocterPatient_PatientID" FOREIGN KEY("PatientID")
REFERENCES "Patient" ("PatientID");

ALTER TABLE "Visit" ADD CONSTRAINT "fk_Visit_PatientID" FOREIGN KEY("PatientID")
REFERENCES "Patient" ("PatientID");

ALTER TABLE "Diagnosis" ADD CONSTRAINT "fk_Diagnosis_PatientID" FOREIGN KEY("PatientID")
REFERENCES "Patient" ("PatientID");

ALTER TABLE "Post" ADD CONSTRAINT "fk_Post_UserID" FOREIGN KEY("UserID")
REFERENCES "User" ("UserID");

ALTER TABLE "Post" ADD CONSTRAINT "fk_Post_CategoryID" FOREIGN KEY("CategoryID")
REFERENCES "Category" ("CategoryID");

ALTER TABLE "Goal" ADD CONSTRAINT "fk_Goal_PlayerID" FOREIGN KEY("PlayerID")
REFERENCES "Player" ("PlayerID");

ALTER TABLE "Player" ADD CONSTRAINT "fk_Player_TeamID" FOREIGN KEY("TeamID")
REFERENCES "Team" ("TeamID");

ALTER TABLE "Match" ADD CONSTRAINT "fk_Match_Team1" FOREIGN KEY("Team1")
REFERENCES "Team" ("TeamID");

ALTER TABLE "Match" ADD CONSTRAINT "fk_Match_Team2" FOREIGN KEY("Team2")
REFERENCES "Team" ("TeamID");

ALTER TABLE "MatchReferee" ADD CONSTRAINT "fk_MatchReferee_MatchID" FOREIGN KEY("MatchID")
REFERENCES "Match" ("MatchID");

ALTER TABLE "MatchReferee" ADD CONSTRAINT "fk_MatchReferee_RefereeID" FOREIGN KEY("RefereeID")
REFERENCES "Referee" ("RefereeID");

-- Free plan table limit reached. SUBSCRIBE for more.



-- Free plan table limit reached. SUBSCRIBE for more.



