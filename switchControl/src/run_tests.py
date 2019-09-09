
import os
import sys
import nose

if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))
    testLoader = nose.loader.TestLoader(workingDir=path)
    nose.main(testLoader=testLoader)

