# List available recipes
default:
    @just --list

# Install everything (mise + ruby gems)
install:
    command -v mise >/dev/null || brew install mise
    mise install
    bundle install

# Build and serve the site locally
serve:
    bundle exec jekyll serve --baseurl "" --livereload

# Build the site for production
build:
    bundle exec jekyll build
