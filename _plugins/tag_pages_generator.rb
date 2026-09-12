# frozen_string_literal: true
class TagPage < Jekyll::PageWithoutAFile
  def initialize(site, base, tag)
    super(site, base, File.join('topics', Jekyll::Utils.slugify(tag)), 'index.html')
    self.data['layout'] = 'tag'
    self.data['title'] = tag
    self.data['tag'] = tag
  end
end

class TagPagesGenerator < Jekyll::Generator
  safe true

  def generate(site)
    tags = site.collections['notes'].docs.flat_map { |note| note.data['tags'] || [] }.compact.uniq.sort
    site.data['tags'] = tags

    tags.each do |tag|
      site.pages << TagPage.new(site, site.source, tag)
    end
  end
end
