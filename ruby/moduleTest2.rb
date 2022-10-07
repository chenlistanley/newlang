#!/usr/bin/ruby
$LOAD_PATH << '.'
require "moduleTest"

def test()
	ModuleA.say()
end

test() 
