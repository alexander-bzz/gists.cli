#!/usr/bin/env python

import sys, actions, log, util, defaults

#-------------------------------------------

_cmds = defaults.cmds

#-------------------------------------------

def _hasCmd( args ):
  log.debug ("_hasCmd: " + str(args))
  if len(args) > 0:
    cmd = args[0]
    # Cmd: is cmd one of the known commands
    if str(cmd).strip().lower() in _cmds['all']:
      log.debug ("_hasCmd: Found")
      return True
    # Shortcut check: is arg a Bool, File, String with spaces/sp char
    if util.parseBool( cmd ) != None:
      return False
    if util.isFileOrDir( cmd ) == True:
      return False
    if str( cmd ).strip().isalnum() == False:
      return False
  return False

#-------------------------------------------

def _deriveCmd( args ):
  log.debug ("_deriveCmd: " + str(args))
  cmd = None
  alen = len(args)

  if alen == 0:
    # list
    cmd = "list"
  elif alen == 1:
    if args[0].strip().isalnum() == True and util.isFileOrDir( args[0] ) == False  and util.parseBool( args[0] ) == None:
      # view ID
      cmd = "view"
    elif util.isFileOrDir( args[0] ) == True:
      # create/new  FILE 
      cmd = "new"
    elif args[0].strip().isalnum() == False:
      # create/new 'Content'
      cmd = "new"
  elif alen == 2:
    if str(args[0]).strip().isalnum() and util.parseBool( args[0] ) == None:
      # get ID 'Dir'
      cmd =  "get"
    else:
      # create/new Boolean and File
      # create/new Boolean and Content
      # create/new Description and File
      # create/new Description and Content
      cmd = "new"
  elif alen == 3 and util.parseBool( args[0] ) != None:
      # create/new Boolean, Description and File
      # create/new Boolean, Description and Content
      cmd = "new"
  return cmd

#-------------------------------------------

def _printNoMatch():
  print 'Unfortunately, no command match found for supplied arguments.'

#-------------------------------------------

def _printNoImpl():
  print 'Unfortunately, this command has not been implemented as yet.'

#-------------------------------------------

def main ( ):

  print ''

  log.setDebug( util.argv( _cmds['Debug'] ) )
  actions.supress( util.argv( _cmds['Supress']) )

  args = sys.argv
  
  if len(args) == 1:
    log.comment ("No arguments specified, listing your Gists. Try '%s help' if you need help." % sys.argv[0])
    print ''

  del args[0] # Delete the filename
  cmd = None

  log.debug ("Arguments " + str( args ))

  #--------------------------------------------
  # If args[0] is a command. We remove it from the list. args now contains only the  command arguments
  # else we keep as is and try to evaluate the command
  #--------------------------------------------
  if _hasCmd( args ):
    cmd = args[0]
    del args[0] # Delete the command. Arguments remaining are the options for each command
  else:
    cmd = _deriveCmd( args )

  log.debug ("Adjusted cmd: " + str(cmd))
  log.debug ("Adjusted arguments " + str( args ))
  #--------------------------------------------
  # Handle commands
  #--------------------------------------------
  if cmd == None:
    _printNoMatch()
  elif cmd in (_cmds['Help']):
    actions.help()
  elif cmd in (_cmds['List']):
    actions.list()
  elif cmd in (_cmds['Token']):
    actions.updateCredentials()
  elif cmd in (_cmds['View']):
    actions.view( args[0] )
  elif cmd in (_cmds['Download']):
    actions.get( args[0], args[1] )
  elif cmd in (_cmds['Append']):
    _printNoImpl()
    actions.append( args[0] )
  elif cmd in (_cmds['Update']):
    _printNoImpl()
    actions.update( args[0] )
  elif cmd in (_cmds['Delete']):
    _printNoImpl()
    actions.delete( args[0] )
  elif cmd in (_cmds['Backup']):
    _printNoImpl()
    actions.backup( )
  elif cmd in (_cmds['Search']):
    _printNoImpl()
    actions.search( )
  elif cmd in (_cmds['New']):
    # Each option will prompt for public/pvt and description. In silent mode, assumes private and no description.
    if len(args) == 0:
      actions.new()
    elif len(args) == 1:
      # create File
      # create Content
      if util.isFileOrDir(args[0]) == True:
        actions.new( filename = args[0] )
      else:
        actions.new( content = args[0] )
    elif len(args) == 2: 
      # create Boolean and File
      # create Boolean and Content
      # create Description and File 
      # create Description and Content 
      if util.parseBool( args[0] ) != None:
        if util.isFileOrDir(args[1]) == True:
          actions.new( public=util.parseBool( args[0] ), filename=args[1] )
        else:
          actions.new( public=util.parseBool( args[0] ), content=args[1] )
      else:
        if util.isFileOrDir(args[1]) == True:
          actions.new( description=args[0], filename=args[1] )
        else:
          actions.new( description=args[0], content=args[1] )
    elif len(args) == 3 and util.parseBool( args[0] ) != None:
      # create Boolean, Description and File
      # create Boolean, Description and Content
      if util.isFileOrDir(args[2]) == True:
        actions.new( public=util.parseBool( args[0] ), description=args[1], filename=args[2] )
      else:
        actions.new( public=util.parseBool( args[0] ), description=args[1], content=args[2] )
    else:
      _printNoMatch()
  else:
    _printNoMatch()

  log.debug ("Done.")
  print ''

#-------------------------------------------

if __name__ == "__main__":
  main ()

#-------------------------------------------
