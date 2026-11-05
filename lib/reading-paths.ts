import data from '../wordpress/plugins/mee-editorial/data/reading-paths.json';

export type ReadingStep = {id:string;title:string;url:string;slug:string;area:string;topic:string;level:string;minutes:number;description:string;keyword:string;purpose:string};
export type ReadingPath = {slug:string;title:string;intro:string;outcome:string;minutes:number;steps:ReadingStep[]};
export const readingPaths: ReadingPath[] = data;
