import os
import pathlib
import shutil

import keras_autodoc


PAGES = {
    'AutoML_for_NeuralNetworks.md': [
        'ai2business.ai_engines.automl_neural_network.AutoMLModels',
    ],
    
}


aliases_needed = [
    'tensorflow.keras.callbacks.Callback',
    'tensorflow.keras.losses.Loss',
    'tensorflow.keras.metrics.Metric',
    'tensorflow.data.Dataset'
]


ROOT = 'https://ai2business.github.io/ai2business/'

ai2business_dir = pathlib.Path(__file__).resolve().parents[1]





def generate(dest_dir):
    template_dir = ai2business_dir / 'docs' / 'templates'
    doc_generator = keras_autodoc.DocumentationGenerator(
        PAGES,
        'https://github.com/ai2business/ai2business/blob/main',
        #template_dir,
        #ai2business_dir / 'examples',
        extra_aliases=aliases_needed,
    )
    doc_generator.generate(dest_dir)
    #readme = (ai2business_dir / 'README.md').read_text()
    #index = (template_dir / 'index.md').read_text()
    #index = index.replace('{{autogenerated}}', readme[readme.find('##'):])
    #(dest_dir / 'index.md').write_text(index, encoding='utf-8')
    #shutil.copyfile(ai2business_dir / '.github' / 'CONTRIBUTING.md',
    #                dest_dir / 'contributing.md')

    #py_to_nb_md(dest_dir)


if __name__ == '__main__':
    generate(ai2business_dir / 'docs' / 'sources')