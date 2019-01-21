Imports System.IO

Partial Class comparefiles
    Inherits System.Web.UI.Page
    Public xmystring As New StringBuilder()

    Protected Sub Page_Load(sender As Object, e As EventArgs) Handles Me.Load
        Dim fp As StreamReader
        Dim precheck As New List(Of String)
        Dim postcheck As New List(Of String)
        xmystring.Clear()
        Dim prefile As String
        Dim postfile As String
        prefile = Request.Form("prechecklist")
        postfile = Request.Form("postchecklist")
        fp = File.OpenText(prefile)
        baseText.InnerText = fp.ReadToEnd()
        fp = File.OpenText(postfile)
        newText.InnerText = fp.ReadToEnd()
        fp.Close()

    End Sub

End Class