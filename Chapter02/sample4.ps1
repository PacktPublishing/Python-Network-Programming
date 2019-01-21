#Powershell sample
function checkgreaternumber($number1,$number2)
{
    if ($number1 -gt $number2)
    {
        write-host ("Greater number is "+$number1)
    }
    else
    {
        write-host ("Greater number is "+$number2)
    }
}

checkgreaternumber 2 3
checkgreaternumber 3 1