import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import List, Tuple
import math

class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def dot(self, other: 'Vector3') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'Vector3') -> 'Vector3':
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitude(self) -> float:
        return math.sqrt(self.dot(self))
    
    def normalize(self) -> 'Vector3':
        mag = self.magnitude()
        return Vector3(self.x/mag, self.y/mag, self.z/mag) if mag != 0 else self
    
    def to_array(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z])

class Matrix4:
    def __init__(self, data: np.ndarray = None):
        self.data = data if data is not None else np.eye(4)
    
    @staticmethod
    def translation(x: float, y: float, z: float) -> 'Matrix4':
        return Matrix4(np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ]))
    
    @staticmethod
    def rotation_x(angle: float) -> 'Matrix4':
        c, s = math.cos(angle), math.sin(angle)
        return Matrix4(np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ]))
    
    @staticmethod
    def rotation_y(angle: float) -> 'Matrix4':
        c, s = math.cos(angle), math.sin(angle)
        return Matrix4(np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ]))
    
    @staticmethod
    def rotation_z(angle: float) -> 'Matrix4':
        c, s = math.cos(angle), math.sin(angle)
        return Matrix4(np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]))
    
    @staticmethod
    def scale(sx: float, sy: float, sz: float) -> 'Matrix4':
        return Matrix4(np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ]))
    
    def __matmul__(self, other: 'Matrix4') -> 'Matrix4':
        return Matrix4(self.data @ other.data)
    
    def transform_point(self, point: Vector3) -> Vector3:
        homogenous = np.array([point.x, point.y, point.z, 1])
        transformed = self.data @ homogenous
        return Vector3(transformed[0], transformed[1], transformed[2])

class Mesh:
    def __init__(self, vertices: List[Vector3], faces: List[Tuple[int, int, int]]):
        self.vertices = vertices
        self.faces = faces
        self.position = Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)
        self.scale = Vector3(1, 1, 1)
    
    def get_transformation_matrix(self) -> Matrix4:
        translation = Matrix4.translation(self.position.x, self.position.y, self.position.z)
        rotation_x = Matrix4.rotation_x(self.rotation.x)
        rotation_y = Matrix4.rotation_y(self.rotation.y)
        rotation_z = Matrix4.rotation_z(self.rotation.z)
        scale = Matrix4.scale(self.scale.x, self.scale.y, self.scale.z)
        
        return translation @ rotation_x @ rotation_y @ rotation_z @ scale
    
    def get_transformed_vertices(self) -> List[Vector3]:
        transform = self.get_transformation_matrix()
        return [transform.transform_point(vertex) for vertex in self.vertices]

class Renderer:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.meshes: List[Mesh] = []
    
    def add_mesh(self, mesh: Mesh):
        self.meshes.append(mesh)
    
    def render(self):
        self.ax.clear()
        
        for mesh in self.meshes:
            vertices = mesh.get_transformed_vertices()
            vertices_array = np.array([v.to_array() for v in vertices])
            
            for face in mesh.faces:
                triangle = vertices_array[list(face)]
                self.ax.plot_trisurf(
                    triangle[:,0], triangle[:,1], triangle[:,2],
                    alpha=0.8, linewidth=0.5
                )
        
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.set_zlim(-5, 5)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        
        plt.show()

# Create a cube mesh
def create_cube() -> Mesh:
    vertices = [
        Vector3(-1, -1, -1), Vector3(1, -1, -1), Vector3(1, 1, -1), Vector3(-1, 1, -1),
        Vector3(-1, -1, 1), Vector3(1, -1, 1), Vector3(1, 1, 1), Vector3(-1, 1, 1)
    ]
    faces = [
        (0, 1, 2), (0, 2, 3),  # front
        (4, 5, 6), (4, 6, 7),  # back
        (0, 4, 7), (0, 7, 3),  # left
        (1, 5, 6), (1, 6, 2),  # right
        (3, 2, 6), (3, 6, 7),  # top
        (0, 1, 5), (0, 5, 4)   # bottom
    ]
    return Mesh(vertices, faces)

# Example usage
renderer = Renderer()
cube = create_cube()
cube.rotation = Vector3(0.5, 0.5, 0)
renderer.add_mesh(cube)
renderer.render()
