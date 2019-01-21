#Powershell Sample code:
$marks=85
if ($marks -le 45)
{
    write-host "Grade C"
}
elseif (($marks -gt 45) -and ($marks -le 75))
{
    write-host "Grade B"
}
elseif ($marks -gt 75)
{
    write-host "Grade A"
}
else
{
    write-host "Unable to determine"
}