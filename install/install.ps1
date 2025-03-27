Write-Host "Installing..."
pip install --upgrade restructuredpython

$input = Read-Host -Prompt "Install Visual Studio Code extension? (y/n)"
if ($input -eq "y" -or $input -eq "Y") {
    Write-Host "Installing extension..."
    code --install-extension RihaanMeher.restructuredpython --force
}