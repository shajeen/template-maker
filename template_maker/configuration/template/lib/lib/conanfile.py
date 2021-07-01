from conans import ConanFile, CMake, tools

class exampleConan(ConanFile):
    name = 'exampleLib'
    version = '0.0.1'
    license = 'MIT'
    description = 'conan library'
    settings = ('os', 'compiler', 'build_type', 'arch')
    exports_sources = '*'
    generators = 'cmake'
    options = {'shared': [True, False]}
    default_options = 'shared=False'
    requires = ('')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy('main.h', dst='include', keep_path=False)
        self.copy('*.dll', dst='bin', keep_path=False)
        self.copy('*.so', dst='lib', keep_path=False)
        self.copy('*.dylib', dst='lib', keep_path=False)
        self.copy('*.lib', dst='lib', keep_path=False)
        self.copy('*.a', dst='lib', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['exampleLib']
