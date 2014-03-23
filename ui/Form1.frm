VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Crew Paring Data Converter"
   ClientHeight    =   4095
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   7215
   LinkTopic       =   "Form1"
   ScaleHeight     =   4095
   ScaleWidth      =   7215
   StartUpPosition =   3  '´°¿ÚÈ±Ê¡
   Begin VB.PictureBox Picture1 
      Height          =   735
      Left            =   0
      Picture         =   "Form1.frx":0000
      ScaleHeight     =   675
      ScaleWidth      =   7155
      TabIndex        =   9
      Top             =   0
      Width           =   7215
   End
   Begin VB.CommandButton Command4 
      Caption         =   "Start Conversion"
      Height          =   495
      Left            =   2040
      TabIndex        =   8
      Top             =   3360
      Width           =   2775
   End
   Begin VB.CommandButton Command3 
      Caption         =   "Choose"
      Height          =   375
      Left            =   4680
      TabIndex        =   7
      Top             =   2160
      Width           =   855
   End
   Begin VB.CommandButton Command2 
      Caption         =   "Choose"
      Height          =   375
      Left            =   2880
      TabIndex        =   3
      Top             =   1560
      Width           =   855
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Choose"
      Height          =   375
      Left            =   2880
      TabIndex        =   2
      Top             =   960
      Width           =   855
   End
   Begin VB.Label Label6 
      Caption         =   "-"
      Height          =   255
      Left            =   360
      TabIndex        =   10
      Top             =   2760
      Width           =   6615
   End
   Begin VB.Label Label5 
      Caption         =   "Where do you want to save the spreadsheet?"
      Height          =   375
      Left            =   360
      TabIndex        =   6
      Top             =   2160
      Width           =   4095
   End
   Begin VB.Label Label4 
      Caption         =   "-"
      Height          =   255
      Left            =   3840
      TabIndex        =   5
      Top             =   1560
      Width           =   3015
   End
   Begin VB.Label Label3 
      Caption         =   "-"
      Height          =   255
      Left            =   3840
      TabIndex        =   4
      Top             =   960
      Width           =   3015
   End
   Begin VB.Label Label2 
      Caption         =   "Please Choose a AOSP file"
      Height          =   255
      Left            =   360
      TabIndex        =   1
      Top             =   1560
      Width           =   2415
   End
   Begin VB.Label Label1 
      Caption         =   "Please Choose a prg file"
      Height          =   255
      Left            =   360
      TabIndex        =   0
      Top             =   960
      Width           =   2415
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
