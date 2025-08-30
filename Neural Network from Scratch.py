import numpy as np
from typing import List, Callable, Tuple

class NeuralNetwork:
    def __init__(self, layers: List[int], 
                 activation: Callable = None,
                 activation_derivative: Callable = None):
        self.layers = layers
        self.weights = []
        self.biases = []
        
        # Xavier initialization
        for i in range(len(layers) - 1):
            limit = np.sqrt(6 / (layers[i] + layers[i+1]))
            self.weights.append(np.random.uniform(-limit, limit, (layers[i], layers[i+1])))
            self.biases.append(np.zeros((1, layers[i+1])))
        
        self.activation = activation or self._sigmoid
        self.activation_derivative = activation_derivative or self._sigmoid_derivative
        
    def _sigmoid(self, x: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def _sigmoid_derivative(self, x: np.ndarray) -> np.ndarray:
        return x * (1 - x)
    
    def _softmax(self, x: np.ndarray) -> np.ndarray:
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def forward(self, X: np.ndarray) -> List[np.ndarray]:
        activations = [X]
        for i in range(len(self.weights)):
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            if i == len(self.weights) - 1:
                a = self._softmax(z)  # Output layer uses softmax
            else:
                a = self.activation(z)
            activations.append(a)
        return activations
    
    def backward(self, X: np.ndarray, y: np.ndarray, learning_rate: float = 0.1):
        activations = self.forward(X)
        m = X.shape[0]
        
        # Output layer error
        error = activations[-1] - y
        deltas = [error]
        
        # Backpropagate
        for i in range(len(self.weights)-1, 0, -1):
            error = deltas[-1].dot(self.weights[i].T) * self.activation_derivative(activations[i])
            deltas.append(error)
        
        deltas.reverse()
        
        # Update weights and biases
        for i in range(len(self.weights)):
            self.weights[i] -= learning_rate * activations[i].T.dot(deltas[i]) / m
            self.biases[i] -= learning_rate * np.sum(deltas[i], axis=0, keepdims=True) / m
    
    def train(self, X: np.ndarray, y: np.ndarray, 
              epochs: int = 1000, learning_rate: float = 0.1,
              batch_size: int = 32, validation_data: Tuple = None):
        
        for epoch in range(epochs):
            # Mini-batch training
            indices = np.random.permutation(X.shape[0])
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            
            for i in range(0, X.shape[0], batch_size):
                X_batch = X_shuffled[i:i+batch_size]
                y_batch = y_shuffled[i:i+batch_size]
                self.backward(X_batch, y_batch, learning_rate)
            
            if validation_data:
                X_val, y_val = validation_data
                predictions = self.predict(X_val)
                accuracy = np.mean(np.argmax(predictions, axis=1) == np.argmax(y_val, axis=1))
                print(f"Epoch {epoch+1}/{epochs}, Validation Accuracy: {accuracy:.4f}")
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.forward(X)[-1]
    
    def predict_classes(self, X: np.ndarray) -> np.ndarray:
        return np.argmax(self.predict(X), axis=1)
