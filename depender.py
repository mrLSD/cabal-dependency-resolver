__author__ = 'Evgeny Ukhanov'
import sys, subprocess

def remover(packages):
    package = packages[len(packages)-1]
    p = subprocess.Popen(['ghc-pkg', 'unregister', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, result = p.communicate()
    if result != '':
        fetch = result.split(': ')
        if len(fetch) > 2:
            new_package = fetch[len(fetch)-1].split(' (')[0].split(' ')
            packages.extend(new_package)
            packages = remover(packages)
    else:
        print('Deleted package: '+package)
    if package in packages:
        packages.remove(package)
    return packages

if len(sys.argv) < 2:
    print('No arguments: exit')
    exit()
packages = []
for arg in rang(1,len(sys.argv)-1)
    packages.append(arg)
while len(remover(packages)):
    pass