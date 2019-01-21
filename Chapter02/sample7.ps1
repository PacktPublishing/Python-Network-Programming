#Powershell Sample Code
Get-Job  #This get the current running threads or Jobs in Powershell
Remove-Job -Force * # This commands closes forcible all the previous threads

$Scriptblock = {
      Param (
         [string]$ipaddress
      )
    if (Test-Connection $ipaddress -quiet)
    { 
        return ("Ping for "+$ipaddress+" is successful")
     }
    else
    {
       return ("Ping for "+$ipaddress+" FAILED") 
    }
   }

$iplist="4.4.4.4","8.8.8.8","10.10.10.10","20.20.20.20","4.2.2.2"

foreach ($ip in $iplist)
{
    Start-Job -ScriptBlock $Scriptblock -ArgumentList $ip | Out-Null
    #The above command is used to invoke the $scriptblock in a multithread
}

#Below logic waits for all the threads or Jobs to get completed
While (@(Get-Job | Where { $_.State -eq "Running" }).Count -ne 0)
  { # Write-Host "Waiting for background jobs..."
     Start-Sleep -Seconds 1
  }

#Below logic is used to print all the values that are returned by each thread and them remove the thread # #or job from memory
ForEach ($Job in (Get-Job)) {
  Receive-Job $Job
  Remove-Job $Job
  }