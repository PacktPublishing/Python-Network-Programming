Imports System.IO
Partial Class selectfiles
    Inherits System.Web.UI.Page
    Public xmystring As New StringBuilder()
  Public tableval As New Hashtable
    Protected Sub Page_Load(sender As Object, e As EventArgs) Handles Me.Load
        Dim precheck As New List(Of String)
        Dim postcheck As New List(Of String)
        Dim prename = New SortedList
        Dim postname = New SortedList
        Dim infoReader As System.IO.FileInfo
    Dim rval as Integer
    rval=0
    
        xmystring.Clear()
        Dim xval As String
    Dim di As New DirectoryInfo("C:\iistest\logs\")
    Dim lFiles As FileInfo() = di.GetFiles("*.txt")
    Dim fi As System.IO.FileSystemInfo
    Dim files() As String = IO.Directory.GetFiles("C:\iistest\logs\", "*.txt", SearchOption.TopDirectoryOnly)
    xmystring.Append("<head><style type='text/css'>a:hover{background:blue;color:yellow;}</style></head>")
        xmystring.Append("<fieldset style='float: left;width: 49%;display: inline-block;box-sizing: border-box;'>")
        xmystring.Append("<legend>Pre check files (Sorted by Last Modified Date)</legend>")

         For Each fi In lFiles
      rval=rval+1
      tableval.add(fi.LastWriteTime.ToString()+rval.tostring(),fi.Name)
            'infoReader = My.Computer.FileSystem.GetFileInfo(file)
            If (fi.Name.Contains("pre")) Then
                precheck.Add(fi.LastWriteTime.ToString()+rval.tostring()) 
            Else
                postcheck.Add(fi.LastWriteTime.ToString()+rval.tostring())
            End If
        Next
        precheck.Sort()
        postcheck.Sort()

        xval = ""
        Dim prekey As ICollection = prename.Keys
        Dim postkey As ICollection = postname.Keys
        Dim dev As String
    Dim fnameval as String
        For Each dev In precheck
            infoReader = My.Computer.FileSystem.GetFileInfo(tableval(dev))
      fnameval="http://localhost/test/logs/"+Path.GetFileName(tableval(dev))
            xval = "<input type = 'radio' name='prechecklist' value='C:\iistest\logs\" + tableval(dev) + "' required><a href='" & fnameval & "' target='blank'>" & tableval(dev) & "</a> ( <b>" & dev.Substring(0,dev.LastIndexOf("M")).Trim() + "M</b>)<br>"
            
      xmystring.Append(xval)
        Next
    xmystring.Append("</fieldset>")
           xmystring.Append("<fieldset style='float: right;width: 49%;display: inline-block;box-sizing: border-box;'>")
        xmystring.Append("<legend>Post check files (Sorted by Last Modified Date)</legend>")
              For Each dev In postcheck
      fnameval="http://localhost/test/logs/"+tableval(dev)
            xval = "<input type = 'radio' name='postchecklist' value='C:\iistest\logs\" + tableval(dev) + "' required><a href='" & fnameval & "' target='blank'>" & tableval(dev) & "</a> ( <b>" & dev.Substring(0,dev.LastIndexOf("M")).Trim() + "M</b>)<br>"
            xmystring.Append(xval)
        Next
        xmystring.Append("</fieldset>")

    End Sub
End Class