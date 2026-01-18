//package equipo._7.SentimentAPI.controller;
//
//import equipo._7.SentimentAPI.domain.user.*;
//import equipo._7.SentimentAPI.infra.security.DataTokenJWT;
//import equipo._7.SentimentAPI.infra.security.TokenService;
//import equipo._7.SentimentAPI.infra.exceptions.ValidacionDeNegocioException; // Importamos la nueva excepción
//import jakarta.transaction.Transactional;
//import jakarta.validation.Valid;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.data.domain.Page;
//import org.springframework.data.domain.Pageable;
//import org.springframework.data.web.PageableDefault;
//import org.springframework.security.authentication.AuthenticationManager;
//import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
//import org.springframework.security.crypto.password.PasswordEncoder;
//import org.springframework.web.bind.annotation.*;
//import org.springframework.http.ResponseEntity;
//
//import java.util.Objects;

<<<<<<< HEAD
//@RestController
//@RequestMapping
//public class AuthController {
//
//    @Autowired
//    private TokenService tokenService;
//    @Autowired
//    private AuthenticationManager manager;
//    @Autowired
//    private UserRepository userRepository;
//    @Autowired
//    private PasswordEncoder passwordEncoder;
//
//    @PostMapping("/login")
//    public ResponseEntity<DataTokenJWT> login(@RequestBody @Valid DataAuth data) {
//        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
//        var auth = manager.authenticate(authToken);
//        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
//        return ResponseEntity.ok(new DataTokenJWT(tokenJwt));
//    }
//
//    @Transactional
//    @PostMapping("/register")
//    public ResponseEntity<DataTokenJWT> register(@RequestBody @Valid DataRegister data) {
//
//        if (!Objects.equals(data.password(), data.passwordConfirmation())) {
//            throw new ValidacionDeNegocioException("Las contraseñas no coinciden");
//        }
//        var user = new User(data.email(), data.name(), encodePassword(data.password()));
//        userRepository.save(user);
//
//        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
//        var auth = manager.authenticate(authToken);
//        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
//
//        return ResponseEntity.ok(new DataTokenJWT(tokenJwt));
//    }
//
//    @GetMapping("/user/{id}")
//    public DataUser getUser(@PathVariable Long id) {
//        var user = userRepository.findById(id);
//        if (user.isEmpty()) {
//            throw new RuntimeException("User not found");
//        }
//        return new DataUser(user.get());
//    }
//
//    @GetMapping("/user")
//    public Page<DataUser> getUsers(@PageableDefault(size = 10, sort = {"name"}) Pageable pageable) {
//        return userRepository.findAll(pageable).map(DataUser::new);
//    }
//
//    @Transactional
//    @DeleteMapping("/user/{id}")
//    public void delete(@PathVariable Long id) {
//        userRepository.deleteById(id);
//    }
//
//    @Transactional
//    @PutMapping("/user/{id}")
//    public DataUser updateUser(@PathVariable Long id, @RequestBody @Valid DataUpdateUser data) {
//        var user = userRepository.findById(id);
//        if (user.isEmpty()) {
//            throw new RuntimeException("User not found");
//        }
//        if (data.name() != null) {
//            user.get().setName(data.name());
//        }
//        if (data.password() != null && Objects.equals(data.passwordConfirmation(), data.password())) {
//            user.get().setPassword(passwordEncoder.encode(data.password()));
//        } else {
//            throw new RuntimeException("Passwords do not match, it requires a confirm password");
//        }
//        return new DataUser(user.get());
//    }
//
//    private String encodePassword(String password) {
//        return passwordEncoder.encode(password);
//    }
//}
=======
import equipo._7.SentimentAPI.domain.user.*;
import equipo._7.SentimentAPI.infra.security.DataTokenJWT;
import equipo._7.SentimentAPI.infra.security.TokenService;
import equipo._7.SentimentAPI.infra.security.exceptions.ValidacionDeNegocioException; // Importamos la nueva excepción
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity; 

import java.util.List;
import java.util.Objects;

@RestController
@RequestMapping
public class AuthController {

    @Autowired
    private TokenService tokenService;
    @Autowired
    private AuthenticationManager manager;
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;

    @PostMapping("/login")
    public ResponseEntity<DataTokenJWT> login(@RequestBody @Valid DataAuth data) {
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        return ResponseEntity.ok(new DataTokenJWT(tokenJwt));
    }

    @Transactional
    @PostMapping("/register")
    public ResponseEntity<DataTokenJWT> register(@RequestBody @Valid DataRegister data) {
    
        if (!Objects.equals(data.password(), data.passwordConfirmation())) {
            throw new ValidacionDeNegocioException("Las contraseñas no coinciden");
        }
        
        var user = new User(data.email(), encodePassword(data.password()));
        userRepository.save(user);
        
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        
        return ResponseEntity.ok(new DataTokenJWT(tokenJwt));
    }

    @GetMapping("/user/{id}")
    public DataUser getUser(@PathVariable Long id) {
        var user = userRepository.findById(id);
        if (user.isEmpty()) {
            throw new RuntimeException("User not found");
        }
        return new DataUser(user.get());
    }

    @GetMapping("/user")
    public Page<DataUser> getUsers(@PageableDefault(size = 10, sort = {"name"}) Pageable pageable) {
        return userRepository.findAll(pageable).map(DataUser::new);
    }

    @Transactional
    @DeleteMapping("/user/{id}")
    public void delete(@PathVariable Long id) {
        userRepository.deleteById(id);
    }

    @Transactional
    @PutMapping("/user/{id}")
    public DataUser updateUser(@PathVariable Long id, @RequestBody @Valid DataUpdateUser data) {
        var user = userRepository.findById(id);
        if (user.isEmpty()) {
            throw new RuntimeException("User not found");
        }
        if (data.name() != null) {
            user.get().setName(data.name());
        }
        if (data.password() != null && Objects.equals(data.passwordConfirmation(), data.password())) {
            user.get().setPassword(passwordEncoder.encode(data.password()));
        } else {
            throw new RuntimeException("Passwords do not match, it requires a confirm password");
        }
        return new DataUser(user.get());
    }

    private String encodePassword(String password) {
        return passwordEncoder.encode(password);
    }
}
>>>>>>> 679119215f769e817ccbe588ab40aed74626e4c0
