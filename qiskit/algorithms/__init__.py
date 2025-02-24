# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=====================================
Algorithms (:mod:`qiskit.algorithms`)
=====================================
It contains a collection of quantum algorithms, for use with quantum computers, to
carry out research and investigate how to solve problems in different domains on
near-term quantum devices with short depth circuits.

Algorithms configuration includes the use of :mod:`~qiskit.algorithms.optimizers` which
were designed to be swappable sub-parts of an algorithm. Any component and may be exchanged for
a different implementation of the same component type in order to potentially alter the behavior
and outcome of the algorithm.

Quantum algorithms are run via a :class:`~qiskit.algorithms.QuantumInstance`
which must be set with the
desired backend where the algorithm's circuits will be executed and be configured with a number of
compile and runtime parameters controlling circuit compilation and execution. It ultimately uses
`Terra <https://www.qiskit.org/terra>`__ for the actual compilation and execution of the quantum
circuits created by the algorithm and its components.

.. currentmodule:: qiskit.algorithms

Algorithms
==========

It contains a variety of quantum algorithms and these have been grouped by logical function such
as minimum eigensolvers and amplitude amplifiers.


Amplitude Amplifiers
--------------------

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   AmplificationProblem
   AmplitudeAmplifier
   Grover
   GroverResult


Amplitude Estimators
--------------------

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   AmplitudeEstimator
   AmplitudeEstimatorResult
   AmplitudeEstimation
   AmplitudeEstimationResult
   EstimationProblem
   FasterAmplitudeEstimation
   FasterAmplitudeEstimationResult
   IterativeAmplitudeEstimation
   IterativeAmplitudeEstimationResult
   MaximumLikelihoodAmplitudeEstimation
   MaximumLikelihoodAmplitudeEstimationResult


Eigensolvers
------------

Algorithms to find eigenvalues of an operator. For chemistry these can be used to find excited
states of a molecule, and qiskit-nature has some algorithms that leverage chemistry specific
knowledge to do this in that application domain.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   Eigensolver
   EigensolverResult

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   NumPyEigensolver
   VQD


Variational Quantum Time Evolution
----------------------------------

Classes used by variational quantum time evolution algorithms - VarQITE and VarQRTE.

.. autosummary::
   :toctree: ../stubs/

   evolvers.variational


Evolvers
--------

Algorithms to evolve quantum states in time. Both real and imaginary time evolution is possible
with algorithms that support them. For machine learning, Quantum Imaginary Time Evolution might be
used to train Quantum Boltzmann Machine Neural Networks for example.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

    RealEvolver
    ImaginaryEvolver
    TrotterQRTE
    VarQITE
    VarQRTE
    PVQD
    PVQDResult
    EvolutionResult
    EvolutionProblem


Factorizers
-----------

Algorithms to find factors of a number.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   Shor
   ShorResult


Linear Solvers
--------------

Algorithms to solve linear systems of equations.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   linear_solvers


Minimum Eigensolvers
--------------------

Algorithms that can find the minimum eigenvalue of an operator.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   MinimumEigensolver
   MinimumEigensolverResult

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   NumPyMinimumEigensolver
   QAOA
   VQE


Optimizers
----------

Classical optimizers for use by quantum variational algorithms.

.. autosummary::
   :toctree: ../stubs/

   optimizers


Phase Estimators
----------------

Algorithms that estimate the phases of eigenstates of a unitary.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   HamiltonianPhaseEstimation
   HamiltonianPhaseEstimationResult
   PhaseEstimationScale
   PhaseEstimation
   PhaseEstimationResult
   IterativePhaseEstimation


Exceptions
==========

.. autosummary::
   :toctree: ../stubs/

   AlgorithmError


Utility methods
---------------

Utility methods used by algorithms.

.. autosummary::
   :toctree: ../stubs/

   eval_observables
"""

from .algorithm_result import AlgorithmResult
from .evolvers import EvolutionResult, EvolutionProblem
from .evolvers.real_evolver import RealEvolver
from .evolvers.imaginary_evolver import ImaginaryEvolver
from .variational_algorithm import VariationalAlgorithm, VariationalResult
from .amplitude_amplifiers import Grover, GroverResult, AmplificationProblem, AmplitudeAmplifier
from .amplitude_estimators import (
    AmplitudeEstimator,
    AmplitudeEstimatorResult,
    AmplitudeEstimation,
    AmplitudeEstimationResult,
    FasterAmplitudeEstimation,
    FasterAmplitudeEstimationResult,
    IterativeAmplitudeEstimation,
    IterativeAmplitudeEstimationResult,
    MaximumLikelihoodAmplitudeEstimation,
    MaximumLikelihoodAmplitudeEstimationResult,
    EstimationProblem,
)
from .eigen_solvers import NumPyEigensolver, Eigensolver, EigensolverResult, VQD, VQDResult
from .factorizers import Shor, ShorResult
from .linear_solvers import HHL, LinearSolver, NumPyLinearSolver, LinearSolverResult
from .minimum_eigen_solvers import (
    VQE,
    VQEResult,
    QAOA,
    NumPyMinimumEigensolver,
    MinimumEigensolver,
    MinimumEigensolverResult,
)
from .phase_estimators import (
    HamiltonianPhaseEstimation,
    HamiltonianPhaseEstimationResult,
    PhaseEstimationScale,
    PhaseEstimation,
    PhaseEstimationResult,
    IterativePhaseEstimation,
)
from .exceptions import AlgorithmError
from .aux_ops_evaluator import eval_observables
from .evolvers.trotterization import TrotterQRTE
from .evolvers.variational.var_qite import VarQITE
from .evolvers.variational.var_qrte import VarQRTE
from .evolvers.pvqd import PVQD, PVQDResult

__all__ = [
    "AlgorithmResult",
    "VariationalAlgorithm",
    "VariationalResult",
    "AmplitudeAmplifier",
    "AmplificationProblem",
    "Grover",
    "GroverResult",
    "AmplitudeEstimator",
    "AmplitudeEstimatorResult",
    "AmplitudeEstimation",
    "AmplitudeEstimationResult",
    "FasterAmplitudeEstimation",
    "FasterAmplitudeEstimationResult",
    "IterativeAmplitudeEstimation",
    "IterativeAmplitudeEstimationResult",
    "MaximumLikelihoodAmplitudeEstimation",
    "MaximumLikelihoodAmplitudeEstimationResult",
    "EstimationProblem",
    "NumPyEigensolver",
    "RealEvolver",
    "ImaginaryEvolver",
    "TrotterQRTE",
    "VarQITE",
    "VarQRTE",
    "EvolutionResult",
    "EvolutionProblem",
    "LinearSolverResult",
    "Eigensolver",
    "EigensolverResult",
    "Shor",
    "ShorResult",
    "VQE",
    "VQEResult",
    "QAOA",
    "LinearSolver",
    "HHL",
    "NumPyLinearSolver",
    "NumPyMinimumEigensolver",
    "MinimumEigensolver",
    "MinimumEigensolverResult",
    "HamiltonianPhaseEstimation",
    "HamiltonianPhaseEstimationResult",
    "VQD",
    "PhaseEstimationScale",
    "PhaseEstimation",
    "PhaseEstimationResult",
    "PVQD",
    "PVQDResult",
    "IterativePhaseEstimation",
    "AlgorithmError",
    "eval_observables",
]
