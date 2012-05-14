{
  'variables': {
    'module_name': 'sapnwrfc',
    'library': 'shared_library',
    'target_arch': 'x64',
    'output_directory': 'Release',
  },

  'targets': [{
    'sources': [
      'src/binding.cc',
      'src/Common.h',
      'src/Connection.h',
      'src/Connection.cc',
      'src/Function.h',
      'src/Function.cc',
    ],
    
    'target_name': '<(module_name)',
    'type': '<(library)',
    'product_name': '<(module_name)',
    'product_extension': 'node',
    'product_dir': '<(output_directory)',
    'product_prefix': '',
    
    'defines': [
      'ARCH="<(target_arch)"',
      'PLATFORM="<(OS)"',
      '_LARGEFILE_SOURCE',
      '_FILE_OFFSET_BITS=64',
      'SAPwithUNICODE',
      'SAPwithTHREADS',
      'NDEBUG',
    ],
    
    'conditions': [
      [ 'OS=="win"', {
        'defines': [
          'PLATFORM="win32"',
          '_X86_',
          'WIN32',
          '_AFXDLL',
          '_CRT_NON_CONFORMING_SWPRINTFS',
          '_CRT_SECURE_NO_DEPRECATE',
          '_CRT_NONSTDC_NO_DEPRECATE',
          'SAPonNT',
          'UNICODE',
          '_UNICODE'
        ],
        'include_dirs': [
          '<(module_root_dir)/nwrfcsdk/include'
        ],
        'msvs_configuration_attributes': {
          'OutputDirectory': '$(SolutionDir)$(ConfigurationName)',
          'IntermediateDirectory': '$(OutDir)\\obj'
        },
        'msvs-settings': {
          'VCLinkerTool': {
            'SubSystem': 3, # /subsystem:dll
            'AdditionalLibraryDirectories': '<(module_root_dir)/nwrfcsdk/lib',
            'AdditionalDependencies': 'sapnwrfc.lib;sapucum.lib',
          },
        },
       'libraries': [ '-lsapnwrfc.lib', '-llibsapucum.lib' ],
      }],
      
      [ 'OS=="mac"', {
      }],
      
      [ 'OS=="linux"', {
        'cflags!': [
          '-Wall',
          '-pedantic'
        ],
        'include_dirs': [
          '/usr/local/include',
	  '/usr/local/include/nwrfcsdk',
	  'nwrfcsdk/include'  # if you symlink nwrfcsdk
        ],
        'defines': [
          'SAPonUNIX',
          'SAPonLIN',
          'SAPwithTHREADS',
          '__NO_MATH_INLINES'
        ],
        'libraries': [ '-lsapnwrfc', '-lsapucum' ],
      }]
    ],
  }] # end targets
}
