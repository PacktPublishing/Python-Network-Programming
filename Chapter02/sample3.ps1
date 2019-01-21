#Powershell Sample code
$countryname=read-host "Enter country name" 
$countryname=$countryname.tolower()
$lastcharacter=$countryname[-1]
if ($lastcharacter -contains 'a')
{
    write-host "Vowel found"
}
elseif ($lastcharacter -contains 'e')
{
    write-host "Vowel found"
}
elseif ($lastcharacter -contains 'i')
{
    write-host "Vowel found"
}
elseif ($lastcharacter -contains '0')
{
    write-host "Vowel found"
}
elseif ($lastcharacter -contains 'u')
{
    write-host "Vowel found"
}
else
{
write-host "No vowel found"
}