# cabal-dependency-resolver
Haskell Cabal packages dependency resolver

## Cabal dependency resolver
It used for Haskell package manager - Cabal. For some various situations when broken packages was appeared. It recursively unregister packages via ghc-pkg and all package depending packages.

## How to use:

* It requered Python 2.7.*
* ghc-pkg
 
> python depender.py package1 [package2 package3 ...]
