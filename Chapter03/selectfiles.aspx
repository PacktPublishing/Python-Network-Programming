<%@ Page Language="VB" AutoEventWireup="false" CodeFile="selectfiles.aspx.vb" Inherits="selectfiles" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" method="post" action="comparefiles.aspx" >
    <div>
    <%response.write(xmystring.tostring())%>
    </div>
         <input type="submit" value="Submit">
    </form>
  <br><br><br>
</body>
</html>