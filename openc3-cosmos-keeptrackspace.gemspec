# encoding: ascii-8bit

# Create the overall gemspec
Gem::Specification.new do |s|
  s.name = 'openc3-cosmos-keeptrackspace'
  s.summary = 'KeepTrack API'
  s.description = <<-EOF
    Enables receiving TLE from KeepTrack API
  EOF
  s.license = 'MIT'
  s.authors = ['Clay Kramp']
  s.email = ['clay@openc3.com']
  s.homepage = 'https://github.com/clayandgen/openc3-cosmos-keeptrackspace'
  s.version = "1.0.0"
  s.platform = Gem::Platform::RUBY

  s.metadata = {
    "source_code_uri" => "https://github.com/clayandgen/openc3-cosmos-keeptrackspace",
    "openc3_minimum_cosmos_version" => "5.0.0",
    "openc3_store_access_type" => "public",
    "openc3_store_keywords" => "KeepTrack, TLE"
  }

  if ENV['VERSION']
    s.version = ENV['VERSION'].dup
  else
    time = Time.now.strftime("%Y%m%d%H%M%S")
    s.version = '0.0.0' + ".#{time}"
  end
  # Prefer pyproject.toml over requirements.txt
  python_dep_file = if File.exist?('pyproject.toml')
    'pyproject.toml'
  else
    'requirements.txt'
  end
  s.files = Dir.glob("{targets,lib,public,tools,microservices}/**/*") + %w(Rakefile README.md LICENSE.txt plugin.txt) + [python_dep_file]
end
