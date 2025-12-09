IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'AtriumDB')
BEGIN
    CREATE DATABASE AtriumDB;
END
GO

USE AtriumDB;
GO

IF OBJECT_ID('UserLikes', 'U') IS NOT NULL DROP TABLE UserLikes;
IF OBJECT_ID('Movies', 'U') IS NOT NULL DROP TABLE Movies;
IF OBJECT_ID('Users', 'U') IS NOT NULL DROP TABLE Users;
GO

CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    FullName NVARCHAR(100) NOT NULL,
    Email NVARCHAR(255) NOT NULL UNIQUE, 
    Password NVARCHAR(255) NOT NULL,
    SubscriptionPlan NVARCHAR(50) DEFAULT 'Free',
    CreatedAt DATETIME DEFAULT GETDATE(),

    CONSTRAINT CK_Password_Complexity CHECK (
        LEN(Password) >= 5 AND 
        Password LIKE '%[0-9]%' AND 
        Password LIKE '%[^a-zA-Z0-9]%' AND 
        CAST(Password AS NVARCHAR(255)) COLLATE Latin1_General_BIN LIKE '%[A-Z]%'
    )
);
GO

CREATE TRIGGER trg_FixEmailDomain
ON Users
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO Users (FullName, Email, Password, SubscriptionPlan, CreatedAt)
    SELECT 
        FullName,
        CASE 
            WHEN CHARINDEX('@', Email) = 0 THEN Email + '@gmail.com'
            ELSE Email 
        END,
        Password,
        COALESCE(SubscriptionPlan, 'Free'), 
        COALESCE(CreatedAt, GETDATE())
    FROM INSERTED;
END;
GO

CREATE TABLE Movies (
    MovieID INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(200) NOT NULL,
    ImageFileName NVARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL DEFAULT 6.0,
    Description NVARCHAR(MAX) NULL
);
GO


CREATE TABLE UserLikes (
    UserID INT NOT NULL,
    MovieID INT NOT NULL,
    LikedAt DATETIME DEFAULT GETDATE(),
    
    CONSTRAINT PK_UserLikes PRIMARY KEY (UserID, MovieID), -- Композитний ключ, щоб не можна було лайкнути двічі
    CONSTRAINT FK_UserLikes_Users FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT FK_UserLikes_Movies FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) ON DELETE CASCADE
);
GO

INSERT INTO Movies (Title, ImageFileName, Price, Description)
VALUES 
('Five', 'Five.png', 6.0, 'Description for Five'),
('Zootopia', 'Zootopia.png', 6.0, 'Description for Zootopia'),
('Tramp', 'Tramp.png', 6.0, 'Description for Tramp'),
('Poppers', 'Poppers.png', 6.0, 'Description for Poppers'),
('Night', 'Night.png', 6.0, 'Description for Night'),
('Alvin', 'Alvin.png', 6.0, 'Description for Alvin'),
('JecyChan', 'JecyChan.png', 6.0, 'Description for JecyChan'),
('Titanic', 'Titanic.png', 6.0, 'Description for Titanic'),
('Game of thrones', 'Game of thrones.png', 6.0, 'Description for Game of thrones'),
('MazeRunner', 'MazeRunner.png', 6.0, 'Description for MazeRunner'),
('Dragon', 'Dragon.png', 6.0, 'Description for Dragon'),
('Pirates', 'Pirates.png', 6.0, 'Description for Pirates'),
('it', 'it.png', 6.0, 'Description for it'),
('Dedpool', 'Dedpool.png', 6.0, 'Description for Dedpool');
GO

INSERT INTO Users (FullName, Email, Password)
VALUES ('Alex Tester', 'alex', 'Pass1!');

SELECT * FROM Users;
GO