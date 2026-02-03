# Use Homebrew Ruby
export PATH := "/opt/homebrew/opt/ruby/bin:" + env_var("PATH")

# Install Ruby dependencies
install:
    bundle install

# Build and serve the site locally
serve:
    bundle exec jekyll serve

# Build the site for production
build:
    bundle exec jekyll build
