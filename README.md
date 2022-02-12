# TypedTree by Brett Kromkamp

[Contextualise](https://contextualise.dev/), a knowledge management application that I am currently developing, allows the user to visualise their topics of interest (that is, *nodes*) and the relationships between those topics (that is, *references to other nodes*) using a network graph visualisation. To that effect, TypedTree makes it straightforward to not only enable the visualisation of the actual (network) graph itself but also to enhance the visualisation with information related to the type of each node and the references to other nodes, respectively.

TypedTree is based on an earlier implementation of mine: [Python tree implementation](https://github.com/caesar0301/treelib).

## Installation

TypedTree officially supports Python 3.7–3.10. To install TypedTree, simply:

    $ pip install --upgrade typed-tree

## Install the Development Version

If you have [Git](https://git-scm.com/) installed on your system, it is possible to install the development version of TypedTree.

Before installing the development version, you may need to uninstall the standard version of TypedTree using ``pip``:

    $ pip uninstall typed-tree

Then do:

    $ git clone https://github.com/brettkromkamp/typed-tree
    $ cd typed-tree
    $ pip install -e .

The ``pip install -e .`` command allows you to follow the development branch as it changes by creating links in the right places and installing the command line scripts to the appropriate locations.

Then, if you want to update TypedTree at any time, in the same directory do:

    $ git pull

## Example
```python
from typedtree.traversalmode import TraversalMode
from typedtree.tree import Tree

tree = Tree()

# A node without a parent pointer is by definition the root node
tree.add_node('Elon Musk', node_type='person')

tree.add_node('Lyndon Rive', parent_pointer='Elon Musk', node_type='person', edge_type='family')
tree.add_node('SpaceX', parent_pointer='Elon Musk', node_type='company', edge_type='founder')
tree.add_node('Tesla', parent_pointer='Elon Musk', node_type='company', edge_type='founder')
tree.add_node('Solar City', parent_pointer='Lyndon Rive', node_type='company', edge_type='co-founder')
tree.add_node('Solar Energy Services', parent_pointer='Solar City', node_type='product', edge_type='service')
tree.add_node('Falcon 9', parent_pointer='SpaceX', node_type='rocket', edge_type='technology')
tree.add_node('Falcon Heavy', parent_pointer='SpaceX', node_type='rocket', edge_type='technology')
tree.add_node('Dragon', parent_pointer='SpaceX', node_type='space-ship', edge_type='technology')
tree.add_node('Model S', parent_pointer='Tesla', node_type='car', edge_type='product')
tree.add_node('Model X', parent_pointer='Tesla', node_type='car', edge_type='product')
tree.add_node('Model Y', parent_pointer='Tesla', node_type='car', edge_type='product')
tree.add_node('Roadster', parent_pointer='Tesla', node_type='car', edge_type='product')

print('\n***** TREE STRUCTURE *****')
tree.display('Elon Musk')

print('\n***** DEPTH-FIRST ITERATION *****')
for node in tree.traverse('Elon Musk'):
    print(f"{node.identifier} [{node.type or '*Undefined*'}]")

print('\n***** BREADTH-FIRST ITERATION *****')
for node in tree.traverse('Elon Musk', mode=TraversalMode.BREADTH):
    print(f"{node.identifier} [{node.type or '*Undefined*'}]")
```

**Output**

```
***** TREE STRUCTURE *****
Elon Musk [person] - (*Undefined*)
        Lyndon Rive [person] - (family)
            Solar City [company] - (co-founder)
                Solar Energy Services [product] - (service)
        SpaceX [company] - (founder)
            Falcon 9 [rocket] - (technology)
            Falcon Heavy [rocket] - (technology)
            Dragon [space-ship] - (technology)
        Tesla [company] - (founder)
            Model S [car] - (product)
            Model X [car] - (product)
            Model Y [car] - (product)
            Roadster [car] - (product)

***** DEPTH-FIRST ITERATION *****
Elon Musk [person]
Lyndon Rive [person]
Solar City [company]
Solar Energy Services [product]
SpaceX [company]
Falcon 9 [rocket]
Falcon Heavy [rocket]
Dragon [space-ship]
Tesla [company]
Model S [car]
Model X [car]
Model Y [car]
Roadster [car]

***** BREADTH-FIRST ITERATION *****
Elon Musk [person]
Lyndon Rive [person]
SpaceX [company]
Tesla [company]
Solar City [company]
Falcon 9 [rocket]
Falcon Heavy [rocket]
Dragon [space-ship]
Model S [car]
Model X [car]
Model Y [car]
Roadster [car]
Solar Energy Services [product]
```

## How to Contribute

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork [the repository](https://github.com/brettkromkamp/typed-tree) on GitHub to start making your changes to the **master** branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published.
