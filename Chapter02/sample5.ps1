#Powershell sample
function checkgreaternumber($number1,$number2)
{
    if ($number1 -gt $number2)
    {
        return $number1
    }
    else
    {
        return $number2
    }
}

write-host ("My greater number in 2 and 4 is ",(checkgreaternumber 2 4))
write-host ("My greater number in 3 and 1 is ",(checkgreaternumber 3 1))