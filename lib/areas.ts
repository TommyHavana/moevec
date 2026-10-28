import taxonomy from "../content/taxonomia.json";
import editorial from "../content/editorial.json";

export type Topic = { slug: string; name: string; children?: Topic[] };
type TaxonomyCategory = { number: number; slug: string; name: string; topics: Topic[]; groups: { slug: string; name: string; topics: Topic[] }[] };
type EditorialCategory = { promise: string; intro: string; detail: string; benefits: { name: string; benefit: string }[] };
export type Area = {
  slug: string;
  name: string;
  claim: string;
  lead: string;
  intro: string;
  detail: string;
  sections: { slug: string; name: string; benefit: string; children: Topic[] }[];
};

// Los nombres proceden del ZIP original. El editorial se sincroniza desde Markdown.
const taxonomyData = taxonomy as unknown as { categories: TaxonomyCategory[] };
const editorialData = editorial as unknown as { categories: EditorialCategory[] };
export const areas: Area[] = taxonomyData.categories.map((category, index) => {
  const copy = editorialData.categories[index];
  const isPolitics = category.number === 7;
  const topics = isPolitics ? category.groups : category.topics;
  return {
    slug: category.slug,
    name: category.name,
    claim: copy.promise,
    lead: copy.promise,
    intro: copy.intro,
    detail: copy.detail,
    sections: topics.map((topic, position) => ({
      slug: topic.slug,
      name: topic.name,
      benefit: copy.benefits[position].benefit,
      children: isPolitics ? category.groups[position].topics : [],
    })),
  };
});

export const blogUrl = process.env.NEXT_PUBLIC_BLOG_URL || "/blog/";
